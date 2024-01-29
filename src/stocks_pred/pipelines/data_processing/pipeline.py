from kedro.pipeline import Pipeline, node, pipeline

from .nodes import download, preprocess_data, split, init_wandb


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=download,
                inputs=['params:symbols'],
                outputs=None,
                name='download_stocks'
                ),
            node(
                func=preprocess_data,
                inputs=['params:data_folder'],
                outputs='dataframe',
                name='preprocess_stocks'
            ),
            node(
                func=init_wandb,
                inputs='params:configg',
                outputs=None,
                name='init_wandb_stocks'
            ),
            node(
                func=split,
                inputs=['dataframe', 'params:random_state', 'params:constring'],
                outputs=['X_train', 'X_test', 'y_train', 'y_test'],
                name='split_stocks'
            )
        ]
    )
