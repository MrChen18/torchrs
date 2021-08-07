from typing import Optional, Callable

import torchvision.transforms as T
import pytorch_lightning as pl
from torch.utils.data import DataLoader

from torchrs.datasets import ADVANCE


class ADVANCEDataModule(pl.LightningDataModule):

    def __init__(
        self,
        root: str = ".data/advance",
        image_transform: T.Compose = T.Compose([T.ToTensor()]),
        audio_transform: T.Compose = T.Compose([]),
        batch_size: int = 1,
        num_workers: int = 0,
        prefetch_factor: int = 2,
        pin_memory: bool = False,
        collate_fn: Optional[Callable] = None
    ):
        super().__init__()
        self.root = root
        self.image_transform = image_transform
        self.audio_transform = audio_transform
        self.batch_size = batch_size
        self.num_workers = num_workers
        self.prefetch_factor = prefetch_factor
        self.pin_memory = pin_memory
        self.collate_fn = collate_fn

    def setup(self, stage: Optional[str] = None):
        self.train_dataset = ADVANCE(
            root=self.root, image_transform=self.image_transform, audio_transform=self.audio_transform
        )

    def train_dataloader(self) -> DataLoader:
        return DataLoader(
            self.train_dataset,
            shuffle=True,
            batch_size=self.batch_size,
            num_workers=self.num_workers,
            prefetch_factor=self.prefetch_factor,
            pin_memory=self.pin_memory,
            collate_fn=self.collate_fn
        )