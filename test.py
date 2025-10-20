data_modalities = widgets.SelectMultiple(
    options=['clinical', 'mRNA', 'DNAm', 'miRNA', 'CNV', 'wsi'],
    index=[0, 1],
    rows=6,
    description='Input data',
    disabled=False
)
display(data_modalities)

dataloaders = utils.get_dataloaders(data_location=DATA,
                                    labels_file='data/labels.tsv',
                                    modalities=data_modalities.value,
                                    wsi_patch_size=299,
                                    n_wsi_patches=5,
#                                     batch_size=20,
#                                     batch_size=64,
#                                     batch_size=32,
#                                     exclude_patients=exclude_cancers,
                                   )


interval_cuts = torch.arange(0., 365 * 5.1, 365 / 2)

labels = [(t, e) for t, e in dataloaders['train'].dataset.label_map.values()]
durations = [t for t, _ in labels]
events = [e for _, e in labels]

interval_cuts = utils.discretize_time_by_duration_quantiles(durations, events, 20)
interval_cuts = torch.from_numpy(interval_cuts)

multisurv = Model(dataloaders=dataloaders,
#                   fusion_method='attention',
#                   output_intervals=interval_cuts,
                  device=device)

print('Output intervals (in years):')
multisurv.output_intervals / 365

multisurv.model_blocks

print('Trainable blocks:')
layer = None

for name, child in multisurv.model.named_children():
    for name_2, params in child.named_parameters():
        if name is not layer:
            print(f'   {name}: {params.requires_grad}')
        layer = name


multisurv.model

multisurv.test_lr_range()
print()

picked_lr = 5e-3

run_tag = utils.compose_run_tag(model=multisurv, lr=picked_lr,
                                dataloaders=dataloaders,
                                log_dir='.training_logs/',
                                suffix='')

fit_args = {
    'lr': picked_lr,
    'num_epochs': 75,
    'info_freq': 5,
#     'info_freq': None,
#     'lr_factor': 0.25,
#     'scheduler_patience': 5,
    'lr_factor': 0.5,
    'scheduler_patience': 10,
    'log_dir': os.path.join('.training_logs/', run_tag),
}

multisurv.fit(**fit_args)

multisurv.best_model_weights.keys()

multisurv.best_concord_values

multisurv.current_concord

multisurv.save_weights(saved_epoch='epoch39', prefix=run_tag, weight_dir=MODELS)
