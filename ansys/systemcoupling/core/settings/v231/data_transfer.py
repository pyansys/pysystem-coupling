#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.systemcoupling.core.settings.datamodel import *

from .data_transfer_child import data_transfer_child


class data_transfer(NamedObject[data_transfer_child]):
    """
    Set data transfer details.
    """

    syc_name = "DataTransfer"

    child_object_type: data_transfer_child = data_transfer_child
    """
    child_object_type of data_transfer.
    """
