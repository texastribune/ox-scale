import factory

from . import models


class DatasetFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Dataset


class DatapointFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Datapoint
    dataset = factory.SubFactory(DatasetFactory)
