from core.shared.base.domain.uuid import UUID


class ItemId(UUID):
    def __init__(self, value: str):
        super().__init__(value)
