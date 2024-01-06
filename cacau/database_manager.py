class DatabaseManager:
    def __init__(self, model):
        self.model = model

    def get_all(self, filters=None):
        filters = {key: value for key, value in filters.dict().items() if value}
        users = self.model.objects.prefetch_related('parent').filter(**filters)
        return users

    def get(self, uuid):
        return self.model.objects.get(uuid=uuid)

    def create(self, payload):
        return self.model.objects.create(**payload.dict())

    def update(self, uuid, payload):
        obj = self.model.objects.get(uuid=uuid)
        for attr, value in payload.dict().items():
            setattr(obj, attr, value)
        obj.asave()
        return obj

    def delete(self, uuid):
        try:
            user = self.model.objects.aget(uuid=uuid)
            user.adelete()
            return True
        except self.model.DoesNotExist:
            return False
