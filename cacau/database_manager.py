class DatabaseManager:
    def __init__(self, model):
        self.model = model

    def get_all(self, filters=None):
        filters = {key: value for key, value in filters.dict().items() if value is not None}
        # users = [user async for user in self.model.objects.filter(**filters)]
        return self.model.objects.filter(**filters)

    def get(self, uuid):
        return self.model.objects.get(uuid=uuid)

    def create(self, payload):
        print(payload.dict())
        return self.model.objects.create(**payload.dict())

    def update(self, uuid, payload):
        obj = self.get(uuid=uuid)
        payload = [(attr, value) for attr, value in payload.dict().items() if value is not None]
        for attr, value in payload:
            setattr(obj, attr, value)
        obj.save()
        return obj

    def delete(self, uuid):
        try:
            user = self.get(uuid=uuid)
            user.delete()
            return True
        except self.model.DoesNotExist:
            return False
