# -*- coding: utf-8 -*-


class Scope(object):
    def apply(self, builder, model):
        """
        Apply the scope to a given query builder.

        :param builder: The query builder
        :type builder: vinor.orm.Builder

        :param model: The model
        :type model: vinor.orm.Model
        """
        raise NotImplementedError
