# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.13.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1PodAffinity(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'preferred_during_scheduling_ignored_during_execution': 'list[V1WeightedPodAffinityTerm]',
        'required_during_scheduling_ignored_during_execution': 'list[V1PodAffinityTerm]'
    }

    attribute_map = {
        'preferred_during_scheduling_ignored_during_execution': 'preferredDuringSchedulingIgnoredDuringExecution',
        'required_during_scheduling_ignored_during_execution': 'requiredDuringSchedulingIgnoredDuringExecution'
    }

    def __init__(self, preferred_during_scheduling_ignored_during_execution=None, required_during_scheduling_ignored_during_execution=None):
        """
        V1PodAffinity - a model defined in Swagger
        """

        self._preferred_during_scheduling_ignored_during_execution = None
        self._required_during_scheduling_ignored_during_execution = None
        self.discriminator = None

        if preferred_during_scheduling_ignored_during_execution is not None:
          self.preferred_during_scheduling_ignored_during_execution = preferred_during_scheduling_ignored_during_execution
        if required_during_scheduling_ignored_during_execution is not None:
          self.required_during_scheduling_ignored_during_execution = required_during_scheduling_ignored_during_execution

    @property
    def preferred_during_scheduling_ignored_during_execution(self):
        """
        Gets the preferred_during_scheduling_ignored_during_execution of this V1PodAffinity.
        The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding \"weight\" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.

        :return: The preferred_during_scheduling_ignored_during_execution of this V1PodAffinity.
        :rtype: list[V1WeightedPodAffinityTerm]
        """
        return self._preferred_during_scheduling_ignored_during_execution

    @preferred_during_scheduling_ignored_during_execution.setter
    def preferred_during_scheduling_ignored_during_execution(self, preferred_during_scheduling_ignored_during_execution):
        """
        Sets the preferred_during_scheduling_ignored_during_execution of this V1PodAffinity.
        The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding \"weight\" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.

        :param preferred_during_scheduling_ignored_during_execution: The preferred_during_scheduling_ignored_during_execution of this V1PodAffinity.
        :type: list[V1WeightedPodAffinityTerm]
        """

        self._preferred_during_scheduling_ignored_during_execution = preferred_during_scheduling_ignored_during_execution

    @property
    def required_during_scheduling_ignored_during_execution(self):
        """
        Gets the required_during_scheduling_ignored_during_execution of this V1PodAffinity.
        If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.

        :return: The required_during_scheduling_ignored_during_execution of this V1PodAffinity.
        :rtype: list[V1PodAffinityTerm]
        """
        return self._required_during_scheduling_ignored_during_execution

    @required_during_scheduling_ignored_during_execution.setter
    def required_during_scheduling_ignored_during_execution(self, required_during_scheduling_ignored_during_execution):
        """
        Sets the required_during_scheduling_ignored_during_execution of this V1PodAffinity.
        If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.

        :param required_during_scheduling_ignored_during_execution: The required_during_scheduling_ignored_during_execution of this V1PodAffinity.
        :type: list[V1PodAffinityTerm]
        """

        self._required_during_scheduling_ignored_during_execution = required_during_scheduling_ignored_during_execution

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1PodAffinity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
