"""This is an auto-generated file.  DO NOT EDIT!"""

from ansys.systemcoupling.core.settings.datamodel import *

SHASH = "9fe2734770a84570cee03cbb2e9745da498baca0427fe4da03d2c4ca814ca521"


class root(Group):
    """
    root object
    """

    syc_name = "SystemCoupling"
    child_names = [
        "activate_hidden",
        "library",
        "coupling_participant",
        "analysis_control",
        "coupling_interface",
        "solution_control",
        "output_control",
    ]

    class activate_hidden(Group):
        """
        'activate_hidden' child of 'root' object
        """

        syc_name = "ActivateHidden"
        property_names_types = [
            ("beta_features", "BetaFeatures", "Boolean"),
            ("alpha_features", "AlphaFeatures", "Boolean"),
            ("lenient_validation", "LenientValidation", "Boolean"),
        ]

        @property
        def beta_features(self) -> Boolean:
            """'beta_features' property of 'root' object"""
            return self.get_property_state("beta_features")

        @beta_features.setter
        def beta_features(self, value: Boolean):
            self.set_property_state("beta_features", value)

        @property
        def alpha_features(self) -> Boolean:
            """'alpha_features' property of 'root' object"""
            return self.get_property_state("alpha_features")

        @alpha_features.setter
        def alpha_features(self, value: Boolean):
            self.set_property_state("alpha_features", value)

        @property
        def lenient_validation(self) -> Boolean:
            """'lenient_validation' property of 'root' object"""
            return self.get_property_state("lenient_validation")

        @lenient_validation.setter
        def lenient_validation(self, value: Boolean):
            self.set_property_state("lenient_validation", value)

    class library(Group):
        """
        'library' child of 'root' object
        """

        syc_name = "Library"
        child_names = [
            "expression",
            "expression_function",
            "reference_frame",
            "instancing",
        ]

        class expression(NamedObject):
            """
            'expression' child of 'library' object
            """

            syc_name = "Expression"

            class child_object_type(Group):
                """
                'child_object_type' child of 'expression' object
                """

                syc_name = "child_object_type"
                property_names_types = [
                    ("expression_name", "ExpressionName", "String"),
                    ("expression_string", "ExpressionString", "String"),
                ]

                @property
                def expression_name(self) -> String:
                    """'expression_name' property of 'expression' object"""
                    return self.get_property_state("expression_name")

                @expression_name.setter
                def expression_name(self, value: String):
                    self.set_property_state("expression_name", value)

                @property
                def expression_string(self) -> String:
                    """'expression_string' property of 'expression' object"""
                    return self.get_property_state("expression_string")

                @expression_string.setter
                def expression_string(self, value: String):
                    self.set_property_state("expression_string", value)

        class expression_function(NamedObject):
            """
            'expression_function' child of 'library' object
            """

            syc_name = "ExpressionFunction"

            class child_object_type(Group):
                """
                'child_object_type' child of 'expression_function' object
                """

                syc_name = "child_object_type"
                property_names_types = [
                    ("module", "Module", "String"),
                    ("function", "Function", "String"),
                    ("function_name", "FunctionName", "String"),
                ]

                @property
                def module(self) -> String:
                    """'module' property of 'expression_function' object"""
                    return self.get_property_state("module")

                @module.setter
                def module(self, value: String):
                    self.set_property_state("module", value)

                @property
                def function(self) -> String:
                    """'function' property of 'expression_function' object"""
                    return self.get_property_state("function")

                @function.setter
                def function(self, value: String):
                    self.set_property_state("function", value)

                @property
                def function_name(self) -> String:
                    """'function_name' property of 'expression_function' object"""
                    return self.get_property_state("function_name")

                @function_name.setter
                def function_name(self, value: String):
                    self.set_property_state("function_name", value)

        class reference_frame(NamedObject):
            """
            'reference_frame' child of 'library' object
            """

            syc_name = "ReferenceFrame"

            class child_object_type(Group):
                """
                'child_object_type' child of 'reference_frame' object
                """

                syc_name = "child_object_type"
                child_names = ["transformation"]

                class transformation(NamedObject):
                    """
                    'transformation' child of 'child_object_type' object
                    """

                    syc_name = "Transformation"

                    class child_object_type(Group):
                        """
                        'child_object_type' child of 'transformation' object
                        """

                        syc_name = "child_object_type"
                        property_names_types = [
                            ("option", "Option", "String"),
                            ("angle", "Angle", "Real"),
                            ("axis", "Axis", "String"),
                            ("vector", "Vector", "RealVector"),
                        ]

                        @property
                        def option(self) -> String:
                            """'option' property of 'transformation' object"""
                            return self.get_property_state("option")

                        @option.setter
                        def option(self, value: String):
                            self.set_property_state("option", value)

                        @property
                        def angle(self) -> Real:
                            """'angle' property of 'transformation' object"""
                            return self.get_property_state("angle")

                        @angle.setter
                        def angle(self, value: Real):
                            self.set_property_state("angle", value)

                        @property
                        def axis(self) -> String:
                            """'axis' property of 'transformation' object"""
                            return self.get_property_state("axis")

                        @axis.setter
                        def axis(self, value: String):
                            self.set_property_state("axis", value)

                        @property
                        def vector(self) -> RealVector:
                            """'vector' property of 'transformation' object"""
                            return self.get_property_state("vector")

                        @vector.setter
                        def vector(self, value: RealVector):
                            self.set_property_state("vector", value)

                property_names_types = [
                    ("option", "Option", "String"),
                    ("parent_reference_frame", "ParentReferenceFrame", "String"),
                    ("transformation_order", "TransformationOrder", "StringList"),
                    ("transformation_matrix", "TransformationMatrix", "RealList"),
                ]

                @property
                def option(self) -> String:
                    """'option' property of 'reference_frame' object"""
                    return self.get_property_state("option")

                @option.setter
                def option(self, value: String):
                    self.set_property_state("option", value)

                @property
                def parent_reference_frame(self) -> String:
                    """'parent_reference_frame' property of 'reference_frame' object"""
                    return self.get_property_state("parent_reference_frame")

                @parent_reference_frame.setter
                def parent_reference_frame(self, value: String):
                    self.set_property_state("parent_reference_frame", value)

                @property
                def transformation_order(self) -> StringList:
                    """'transformation_order' property of 'reference_frame' object"""
                    return self.get_property_state("transformation_order")

                @transformation_order.setter
                def transformation_order(self, value: StringList):
                    self.set_property_state("transformation_order", value)

                @property
                def transformation_matrix(self) -> RealList:
                    """'transformation_matrix' property of 'reference_frame' object"""
                    return self.get_property_state("transformation_matrix")

                @transformation_matrix.setter
                def transformation_matrix(self, value: RealList):
                    self.set_property_state("transformation_matrix", value)

        class instancing(NamedObject):
            """
            'instancing' child of 'library' object
            """

            syc_name = "Instancing"

            class child_object_type(Group):
                """
                'child_object_type' child of 'instancing' object
                """

                syc_name = "child_object_type"
                property_names_types = [
                    ("reference_frame", "ReferenceFrame", "String"),
                    ("instances_in_full_circle", "InstancesInFullCircle", "Integer"),
                    ("instances_for_mapping", "InstancesForMapping", "Integer"),
                ]

                @property
                def reference_frame(self) -> String:
                    """'reference_frame' property of 'instancing' object"""
                    return self.get_property_state("reference_frame")

                @reference_frame.setter
                def reference_frame(self, value: String):
                    self.set_property_state("reference_frame", value)

                @property
                def instances_in_full_circle(self) -> Integer:
                    """'instances_in_full_circle' property of 'instancing' object"""
                    return self.get_property_state("instances_in_full_circle")

                @instances_in_full_circle.setter
                def instances_in_full_circle(self, value: Integer):
                    self.set_property_state("instances_in_full_circle", value)

                @property
                def instances_for_mapping(self) -> Integer:
                    """'instances_for_mapping' property of 'instancing' object"""
                    return self.get_property_state("instances_for_mapping")

                @instances_for_mapping.setter
                def instances_for_mapping(self, value: Integer):
                    self.set_property_state("instances_for_mapping", value)

    class coupling_participant(NamedObject):
        """
        'coupling_participant' child of 'root' object
        """

        syc_name = "CouplingParticipant"

        class child_object_type(Group):
            """
            'child_object_type' child of 'coupling_participant' object
            """

            syc_name = "child_object_type"
            child_names = [
                "variable",
                "region",
                "update_control",
                "fmu_parameter",
                "execution_control",
                "external_data_file",
            ]

            class variable(NamedObject):
                """
                'variable' child of 'child_object_type' object
                """

                syc_name = "Variable"

                class child_object_type(Group):
                    """
                    'child_object_type' child of 'variable' object
                    """

                    syc_name = "child_object_type"
                    child_names = ["attribute"]

                    class attribute(NamedObject):
                        """
                        'attribute' child of 'child_object_type' object
                        """

                        syc_name = "Attribute"

                        class child_object_type(Group):
                            """
                            'child_object_type' child of 'attribute' object
                            """

                            syc_name = "child_object_type"
                            child_names = ["dimensionality"]

                            class dimensionality(Group):
                                """
                                'dimensionality' child of 'child_object_type' object
                                """

                                syc_name = "Dimensionality"
                                property_names_types = [
                                    ("length", "Length", "Real"),
                                    ("time", "Time", "Real"),
                                    ("mass", "Mass", "Real"),
                                    ("temperature", "Temperature", "Real"),
                                    (
                                        "amount_of_substance",
                                        "AmountOfSubstance",
                                        "Real",
                                    ),
                                    ("current", "Current", "Real"),
                                    ("luminous_intensity", "LuminousIntensity", "Real"),
                                    ("angle", "Angle", "Real"),
                                ]

                                @property
                                def length(self) -> Real:
                                    """'length' property of 'child_object_type' object"""
                                    return self.get_property_state("length")

                                @length.setter
                                def length(self, value: Real):
                                    self.set_property_state("length", value)

                                @property
                                def time(self) -> Real:
                                    """'time' property of 'child_object_type' object"""
                                    return self.get_property_state("time")

                                @time.setter
                                def time(self, value: Real):
                                    self.set_property_state("time", value)

                                @property
                                def mass(self) -> Real:
                                    """'mass' property of 'child_object_type' object"""
                                    return self.get_property_state("mass")

                                @mass.setter
                                def mass(self, value: Real):
                                    self.set_property_state("mass", value)

                                @property
                                def temperature(self) -> Real:
                                    """'temperature' property of 'child_object_type' object"""
                                    return self.get_property_state("temperature")

                                @temperature.setter
                                def temperature(self, value: Real):
                                    self.set_property_state("temperature", value)

                                @property
                                def amount_of_substance(self) -> Real:
                                    """'amount_of_substance' property of 'child_object_type' object"""
                                    return self.get_property_state(
                                        "amount_of_substance"
                                    )

                                @amount_of_substance.setter
                                def amount_of_substance(self, value: Real):
                                    self.set_property_state(
                                        "amount_of_substance", value
                                    )

                                @property
                                def current(self) -> Real:
                                    """'current' property of 'child_object_type' object"""
                                    return self.get_property_state("current")

                                @current.setter
                                def current(self, value: Real):
                                    self.set_property_state("current", value)

                                @property
                                def luminous_intensity(self) -> Real:
                                    """'luminous_intensity' property of 'child_object_type' object"""
                                    return self.get_property_state("luminous_intensity")

                                @luminous_intensity.setter
                                def luminous_intensity(self, value: Real):
                                    self.set_property_state("luminous_intensity", value)

                                @property
                                def angle(self) -> Real:
                                    """'angle' property of 'child_object_type' object"""
                                    return self.get_property_state("angle")

                                @angle.setter
                                def angle(self, value: Real):
                                    self.set_property_state("angle", value)

                            property_names_types = [
                                ("attribute_type", "AttributeType", "String"),
                                ("real_value", "RealValue", "Real"),
                                ("integer_value", "IntegerValue", "Integer"),
                            ]

                            @property
                            def attribute_type(self) -> String:
                                """'attribute_type' property of 'attribute' object"""
                                return self.get_property_state("attribute_type")

                            @attribute_type.setter
                            def attribute_type(self, value: String):
                                self.set_property_state("attribute_type", value)

                            @property
                            def real_value(self) -> Real:
                                """'real_value' property of 'attribute' object"""
                                return self.get_property_state("real_value")

                            @real_value.setter
                            def real_value(self, value: Real):
                                self.set_property_state("real_value", value)

                            @property
                            def integer_value(self) -> Integer:
                                """'integer_value' property of 'attribute' object"""
                                return self.get_property_state("integer_value")

                            @integer_value.setter
                            def integer_value(self, value: Integer):
                                self.set_property_state("integer_value", value)

                    property_names_types = [
                        ("quantity_type", "QuantityType", "String"),
                        ("location", "Location", "String"),
                        (
                            "participant_display_name",
                            "ParticipantDisplayName",
                            "String",
                        ),
                        ("display_name", "DisplayName", "String"),
                        ("data_type", "DataType", "String"),
                        ("real_initial_value", "RealInitialValue", "Real"),
                        ("integer_initial_value", "IntegerInitialValue", "Integer"),
                        ("logical_initial_value", "LogicalInitialValue", "Boolean"),
                        ("string_initial_value", "StringInitialValue", "String"),
                        ("real_min", "RealMin", "Real"),
                        ("real_max", "RealMax", "Real"),
                        ("integer_min", "IntegerMin", "Integer"),
                        ("integer_max", "IntegerMax", "Integer"),
                        ("tensor_type", "TensorType", "String"),
                        ("is_extensive", "IsExtensive", "Boolean"),
                    ]

                    @property
                    def quantity_type(self) -> String:
                        """'quantity_type' property of 'variable' object"""
                        return self.get_property_state("quantity_type")

                    @quantity_type.setter
                    def quantity_type(self, value: String):
                        self.set_property_state("quantity_type", value)

                    @property
                    def location(self) -> String:
                        """'location' property of 'variable' object"""
                        return self.get_property_state("location")

                    @location.setter
                    def location(self, value: String):
                        self.set_property_state("location", value)

                    @property
                    def participant_display_name(self) -> String:
                        """'participant_display_name' property of 'variable' object"""
                        return self.get_property_state("participant_display_name")

                    @participant_display_name.setter
                    def participant_display_name(self, value: String):
                        self.set_property_state("participant_display_name", value)

                    @property
                    def display_name(self) -> String:
                        """'display_name' property of 'variable' object"""
                        return self.get_property_state("display_name")

                    @display_name.setter
                    def display_name(self, value: String):
                        self.set_property_state("display_name", value)

                    @property
                    def data_type(self) -> String:
                        """'data_type' property of 'variable' object"""
                        return self.get_property_state("data_type")

                    @data_type.setter
                    def data_type(self, value: String):
                        self.set_property_state("data_type", value)

                    @property
                    def real_initial_value(self) -> Real:
                        """'real_initial_value' property of 'variable' object"""
                        return self.get_property_state("real_initial_value")

                    @real_initial_value.setter
                    def real_initial_value(self, value: Real):
                        self.set_property_state("real_initial_value", value)

                    @property
                    def integer_initial_value(self) -> Integer:
                        """'integer_initial_value' property of 'variable' object"""
                        return self.get_property_state("integer_initial_value")

                    @integer_initial_value.setter
                    def integer_initial_value(self, value: Integer):
                        self.set_property_state("integer_initial_value", value)

                    @property
                    def logical_initial_value(self) -> Boolean:
                        """'logical_initial_value' property of 'variable' object"""
                        return self.get_property_state("logical_initial_value")

                    @logical_initial_value.setter
                    def logical_initial_value(self, value: Boolean):
                        self.set_property_state("logical_initial_value", value)

                    @property
                    def string_initial_value(self) -> String:
                        """'string_initial_value' property of 'variable' object"""
                        return self.get_property_state("string_initial_value")

                    @string_initial_value.setter
                    def string_initial_value(self, value: String):
                        self.set_property_state("string_initial_value", value)

                    @property
                    def real_min(self) -> Real:
                        """'real_min' property of 'variable' object"""
                        return self.get_property_state("real_min")

                    @real_min.setter
                    def real_min(self, value: Real):
                        self.set_property_state("real_min", value)

                    @property
                    def real_max(self) -> Real:
                        """'real_max' property of 'variable' object"""
                        return self.get_property_state("real_max")

                    @real_max.setter
                    def real_max(self, value: Real):
                        self.set_property_state("real_max", value)

                    @property
                    def integer_min(self) -> Integer:
                        """'integer_min' property of 'variable' object"""
                        return self.get_property_state("integer_min")

                    @integer_min.setter
                    def integer_min(self, value: Integer):
                        self.set_property_state("integer_min", value)

                    @property
                    def integer_max(self) -> Integer:
                        """'integer_max' property of 'variable' object"""
                        return self.get_property_state("integer_max")

                    @integer_max.setter
                    def integer_max(self, value: Integer):
                        self.set_property_state("integer_max", value)

                    @property
                    def tensor_type(self) -> String:
                        """'tensor_type' property of 'variable' object"""
                        return self.get_property_state("tensor_type")

                    @tensor_type.setter
                    def tensor_type(self, value: String):
                        self.set_property_state("tensor_type", value)

                    @property
                    def is_extensive(self) -> Boolean:
                        """'is_extensive' property of 'variable' object"""
                        return self.get_property_state("is_extensive")

                    @is_extensive.setter
                    def is_extensive(self, value: Boolean):
                        self.set_property_state("is_extensive", value)

            class region(NamedObject):
                """
                'region' child of 'child_object_type' object
                """

                syc_name = "Region"

                class child_object_type(Group):
                    """
                    'child_object_type' child of 'region' object
                    """

                    syc_name = "child_object_type"
                    property_names_types = [
                        ("topology", "Topology", "String"),
                        ("input_variables", "InputVariables", "StringList"),
                        ("output_variables", "OutputVariables", "StringList"),
                        ("display_name", "DisplayName", "String"),
                        (
                            "region_discretization_type",
                            "RegionDiscretizationType",
                            "String",
                        ),
                    ]

                    @property
                    def topology(self) -> String:
                        """'topology' property of 'region' object"""
                        return self.get_property_state("topology")

                    @topology.setter
                    def topology(self, value: String):
                        self.set_property_state("topology", value)

                    @property
                    def input_variables(self) -> StringList:
                        """'input_variables' property of 'region' object"""
                        return self.get_property_state("input_variables")

                    @input_variables.setter
                    def input_variables(self, value: StringList):
                        self.set_property_state("input_variables", value)

                    @property
                    def output_variables(self) -> StringList:
                        """'output_variables' property of 'region' object"""
                        return self.get_property_state("output_variables")

                    @output_variables.setter
                    def output_variables(self, value: StringList):
                        self.set_property_state("output_variables", value)

                    @property
                    def display_name(self) -> String:
                        """'display_name' property of 'region' object"""
                        return self.get_property_state("display_name")

                    @display_name.setter
                    def display_name(self, value: String):
                        self.set_property_state("display_name", value)

                    @property
                    def region_discretization_type(self) -> String:
                        """'region_discretization_type' property of 'region' object"""
                        return self.get_property_state("region_discretization_type")

                    @region_discretization_type.setter
                    def region_discretization_type(self, value: String):
                        self.set_property_state("region_discretization_type", value)

            class update_control(Group):
                """
                'update_control' child of 'child_object_type' object
                """

                syc_name = "UpdateControl"
                property_names_types = [
                    ("option", "Option", "String"),
                    ("update_frequency", "UpdateFrequency", "Integer"),
                ]

                @property
                def option(self) -> String:
                    """'option' property of 'child_object_type' object"""
                    return self.get_property_state("option")

                @option.setter
                def option(self, value: String):
                    self.set_property_state("option", value)

                @property
                def update_frequency(self) -> Integer:
                    """'update_frequency' property of 'child_object_type' object"""
                    return self.get_property_state("update_frequency")

                @update_frequency.setter
                def update_frequency(self, value: Integer):
                    self.set_property_state("update_frequency", value)

            class fmu_parameter(NamedObject):
                """
                'fmu_parameter' child of 'child_object_type' object
                """

                syc_name = "FMUParameter"

                class child_object_type(Group):
                    """
                    'child_object_type' child of 'fmu_parameter' object
                    """

                    syc_name = "child_object_type"
                    property_names_types = [
                        ("data_type", "DataType", "String"),
                        (
                            "participant_display_name",
                            "ParticipantDisplayName",
                            "String",
                        ),
                        ("display_name", "DisplayName", "String"),
                        ("real_value", "RealValue", "Real"),
                        ("real_min", "RealMin", "Real"),
                        ("real_max", "RealMax", "Real"),
                        ("integer_value", "IntegerValue", "Integer"),
                        ("integer_min", "IntegerMin", "Integer"),
                        ("integer_max", "IntegerMax", "Integer"),
                        ("logical_value", "LogicalValue", "Boolean"),
                        ("string_value", "StringValue", "String"),
                    ]

                    @property
                    def data_type(self) -> String:
                        """'data_type' property of 'fmu_parameter' object"""
                        return self.get_property_state("data_type")

                    @data_type.setter
                    def data_type(self, value: String):
                        self.set_property_state("data_type", value)

                    @property
                    def participant_display_name(self) -> String:
                        """'participant_display_name' property of 'fmu_parameter' object"""
                        return self.get_property_state("participant_display_name")

                    @participant_display_name.setter
                    def participant_display_name(self, value: String):
                        self.set_property_state("participant_display_name", value)

                    @property
                    def display_name(self) -> String:
                        """'display_name' property of 'fmu_parameter' object"""
                        return self.get_property_state("display_name")

                    @display_name.setter
                    def display_name(self, value: String):
                        self.set_property_state("display_name", value)

                    @property
                    def real_value(self) -> Real:
                        """'real_value' property of 'fmu_parameter' object"""
                        return self.get_property_state("real_value")

                    @real_value.setter
                    def real_value(self, value: Real):
                        self.set_property_state("real_value", value)

                    @property
                    def real_min(self) -> Real:
                        """'real_min' property of 'fmu_parameter' object"""
                        return self.get_property_state("real_min")

                    @real_min.setter
                    def real_min(self, value: Real):
                        self.set_property_state("real_min", value)

                    @property
                    def real_max(self) -> Real:
                        """'real_max' property of 'fmu_parameter' object"""
                        return self.get_property_state("real_max")

                    @real_max.setter
                    def real_max(self, value: Real):
                        self.set_property_state("real_max", value)

                    @property
                    def integer_value(self) -> Integer:
                        """'integer_value' property of 'fmu_parameter' object"""
                        return self.get_property_state("integer_value")

                    @integer_value.setter
                    def integer_value(self, value: Integer):
                        self.set_property_state("integer_value", value)

                    @property
                    def integer_min(self) -> Integer:
                        """'integer_min' property of 'fmu_parameter' object"""
                        return self.get_property_state("integer_min")

                    @integer_min.setter
                    def integer_min(self, value: Integer):
                        self.set_property_state("integer_min", value)

                    @property
                    def integer_max(self) -> Integer:
                        """'integer_max' property of 'fmu_parameter' object"""
                        return self.get_property_state("integer_max")

                    @integer_max.setter
                    def integer_max(self, value: Integer):
                        self.set_property_state("integer_max", value)

                    @property
                    def logical_value(self) -> Boolean:
                        """'logical_value' property of 'fmu_parameter' object"""
                        return self.get_property_state("logical_value")

                    @logical_value.setter
                    def logical_value(self, value: Boolean):
                        self.set_property_state("logical_value", value)

                    @property
                    def string_value(self) -> String:
                        """'string_value' property of 'fmu_parameter' object"""
                        return self.get_property_state("string_value")

                    @string_value.setter
                    def string_value(self, value: String):
                        self.set_property_state("string_value", value)

            class execution_control(Group):
                """
                'execution_control' child of 'child_object_type' object
                """

                syc_name = "ExecutionControl"
                child_names = ["fluent_input"]

                class fluent_input(Group):
                    """
                    'fluent_input' child of 'execution_control' object
                    """

                    syc_name = "FluentInput"
                    property_names_types = [
                        ("option", "Option", "String"),
                        ("case_file", "CaseFile", "String"),
                        ("data_file", "DataFile", "String"),
                        ("journal_file", "JournalFile", "String"),
                    ]

                    @property
                    def option(self) -> String:
                        """'option' property of 'execution_control' object"""
                        return self.get_property_state("option")

                    @option.setter
                    def option(self, value: String):
                        self.set_property_state("option", value)

                    @property
                    def case_file(self) -> String:
                        """'case_file' property of 'execution_control' object"""
                        return self.get_property_state("case_file")

                    @case_file.setter
                    def case_file(self, value: String):
                        self.set_property_state("case_file", value)

                    @property
                    def data_file(self) -> String:
                        """'data_file' property of 'execution_control' object"""
                        return self.get_property_state("data_file")

                    @data_file.setter
                    def data_file(self, value: String):
                        self.set_property_state("data_file", value)

                    @property
                    def journal_file(self) -> String:
                        """'journal_file' property of 'execution_control' object"""
                        return self.get_property_state("journal_file")

                    @journal_file.setter
                    def journal_file(self, value: String):
                        self.set_property_state("journal_file", value)

                property_names_types = [
                    ("option", "Option", "String"),
                    ("working_directory", "WorkingDirectory", "String"),
                    ("executable", "Executable", "String"),
                    (
                        "auto_distribution_settings",
                        "AutoDistributionSettings",
                        "Boolean",
                    ),
                    (
                        "include_hpc_distribution_types",
                        "IncludeHPCDistributionTypes",
                        "StringList",
                    ),
                    ("number_of_cores_per_task", "NumberOfCoresPerTask", "Integer"),
                    ("batch_options", "BatchOptions", "String"),
                    ("additional_arguments", "AdditionalArguments", "String"),
                    ("parallel_fraction", "ParallelFraction", "Real"),
                    ("initial_input", "InitialInput", "String"),
                    (
                        "additional_restart_input_file",
                        "AdditionalRestartInputFile",
                        "String",
                    ),
                    ("gui_mode", "GuiMode", "Boolean"),
                    ("base_output_file_name", "BaseOutputFileName", "String"),
                    ("overwrite_existing_files", "OverwriteExistingFiles", "Boolean"),
                ]

                @property
                def option(self) -> String:
                    """'option' property of 'child_object_type' object"""
                    return self.get_property_state("option")

                @option.setter
                def option(self, value: String):
                    self.set_property_state("option", value)

                @property
                def working_directory(self) -> String:
                    """'working_directory' property of 'child_object_type' object"""
                    return self.get_property_state("working_directory")

                @working_directory.setter
                def working_directory(self, value: String):
                    self.set_property_state("working_directory", value)

                @property
                def executable(self) -> String:
                    """'executable' property of 'child_object_type' object"""
                    return self.get_property_state("executable")

                @executable.setter
                def executable(self, value: String):
                    self.set_property_state("executable", value)

                @property
                def auto_distribution_settings(self) -> Boolean:
                    """'auto_distribution_settings' property of 'child_object_type' object"""
                    return self.get_property_state("auto_distribution_settings")

                @auto_distribution_settings.setter
                def auto_distribution_settings(self, value: Boolean):
                    self.set_property_state("auto_distribution_settings", value)

                @property
                def include_hpc_distribution_types(self) -> StringList:
                    """'include_hpc_distribution_types' property of 'child_object_type' object"""
                    return self.get_property_state("include_hpc_distribution_types")

                @include_hpc_distribution_types.setter
                def include_hpc_distribution_types(self, value: StringList):
                    self.set_property_state("include_hpc_distribution_types", value)

                @property
                def number_of_cores_per_task(self) -> Integer:
                    """'number_of_cores_per_task' property of 'child_object_type' object"""
                    return self.get_property_state("number_of_cores_per_task")

                @number_of_cores_per_task.setter
                def number_of_cores_per_task(self, value: Integer):
                    self.set_property_state("number_of_cores_per_task", value)

                @property
                def batch_options(self) -> String:
                    """'batch_options' property of 'child_object_type' object"""
                    return self.get_property_state("batch_options")

                @batch_options.setter
                def batch_options(self, value: String):
                    self.set_property_state("batch_options", value)

                @property
                def additional_arguments(self) -> String:
                    """'additional_arguments' property of 'child_object_type' object"""
                    return self.get_property_state("additional_arguments")

                @additional_arguments.setter
                def additional_arguments(self, value: String):
                    self.set_property_state("additional_arguments", value)

                @property
                def parallel_fraction(self) -> Real:
                    """'parallel_fraction' property of 'child_object_type' object"""
                    return self.get_property_state("parallel_fraction")

                @parallel_fraction.setter
                def parallel_fraction(self, value: Real):
                    self.set_property_state("parallel_fraction", value)

                @property
                def initial_input(self) -> String:
                    """'initial_input' property of 'child_object_type' object"""
                    return self.get_property_state("initial_input")

                @initial_input.setter
                def initial_input(self, value: String):
                    self.set_property_state("initial_input", value)

                @property
                def additional_restart_input_file(self) -> String:
                    """'additional_restart_input_file' property of 'child_object_type' object"""
                    return self.get_property_state("additional_restart_input_file")

                @additional_restart_input_file.setter
                def additional_restart_input_file(self, value: String):
                    self.set_property_state("additional_restart_input_file", value)

                @property
                def gui_mode(self) -> Boolean:
                    """'gui_mode' property of 'child_object_type' object"""
                    return self.get_property_state("gui_mode")

                @gui_mode.setter
                def gui_mode(self, value: Boolean):
                    self.set_property_state("gui_mode", value)

                @property
                def base_output_file_name(self) -> String:
                    """'base_output_file_name' property of 'child_object_type' object"""
                    return self.get_property_state("base_output_file_name")

                @base_output_file_name.setter
                def base_output_file_name(self, value: String):
                    self.set_property_state("base_output_file_name", value)

                @property
                def overwrite_existing_files(self) -> Boolean:
                    """'overwrite_existing_files' property of 'child_object_type' object"""
                    return self.get_property_state("overwrite_existing_files")

                @overwrite_existing_files.setter
                def overwrite_existing_files(self, value: Boolean):
                    self.set_property_state("overwrite_existing_files", value)

            class external_data_file(Group):
                """
                'external_data_file' child of 'child_object_type' object
                """

                syc_name = "ExternalDataFile"
                property_names_types = [("file_path", "FilePath", "String")]

                @property
                def file_path(self) -> String:
                    """'file_path' property of 'child_object_type' object"""
                    return self.get_property_state("file_path")

                @file_path.setter
                def file_path(self, value: String):
                    self.set_property_state("file_path", value)

            property_names_types = [
                ("participant_type", "ParticipantType", "String"),
                ("participant_display_name", "ParticipantDisplayName", "String"),
                ("display_name", "DisplayName", "String"),
                ("dimension", "Dimension", "String"),
                ("participant_file_loaded", "ParticipantFileLoaded", "String"),
                ("logging_on", "LoggingOn", "Boolean"),
                ("participant_analysis_type", "ParticipantAnalysisType", "String"),
                ("use_new_ap_is", "UseNewAPIs", "Boolean"),
                ("restarts_supported", "RestartsSupported", "Boolean"),
            ]

            @property
            def participant_type(self) -> String:
                """'participant_type' property of 'coupling_participant' object"""
                return self.get_property_state("participant_type")

            @participant_type.setter
            def participant_type(self, value: String):
                self.set_property_state("participant_type", value)

            @property
            def participant_display_name(self) -> String:
                """'participant_display_name' property of 'coupling_participant' object"""
                return self.get_property_state("participant_display_name")

            @participant_display_name.setter
            def participant_display_name(self, value: String):
                self.set_property_state("participant_display_name", value)

            @property
            def display_name(self) -> String:
                """'display_name' property of 'coupling_participant' object"""
                return self.get_property_state("display_name")

            @display_name.setter
            def display_name(self, value: String):
                self.set_property_state("display_name", value)

            @property
            def dimension(self) -> String:
                """'dimension' property of 'coupling_participant' object"""
                return self.get_property_state("dimension")

            @dimension.setter
            def dimension(self, value: String):
                self.set_property_state("dimension", value)

            @property
            def participant_file_loaded(self) -> String:
                """'participant_file_loaded' property of 'coupling_participant' object"""
                return self.get_property_state("participant_file_loaded")

            @participant_file_loaded.setter
            def participant_file_loaded(self, value: String):
                self.set_property_state("participant_file_loaded", value)

            @property
            def logging_on(self) -> Boolean:
                """'logging_on' property of 'coupling_participant' object"""
                return self.get_property_state("logging_on")

            @logging_on.setter
            def logging_on(self, value: Boolean):
                self.set_property_state("logging_on", value)

            @property
            def participant_analysis_type(self) -> String:
                """'participant_analysis_type' property of 'coupling_participant' object"""
                return self.get_property_state("participant_analysis_type")

            @participant_analysis_type.setter
            def participant_analysis_type(self, value: String):
                self.set_property_state("participant_analysis_type", value)

            @property
            def use_new_ap_is(self) -> Boolean:
                """'use_new_ap_is' property of 'coupling_participant' object"""
                return self.get_property_state("use_new_ap_is")

            @use_new_ap_is.setter
            def use_new_ap_is(self, value: Boolean):
                self.set_property_state("use_new_ap_is", value)

            @property
            def restarts_supported(self) -> Boolean:
                """'restarts_supported' property of 'coupling_participant' object"""
                return self.get_property_state("restarts_supported")

            @restarts_supported.setter
            def restarts_supported(self, value: Boolean):
                self.set_property_state("restarts_supported", value)

    class analysis_control(Group):
        """
        'analysis_control' child of 'root' object
        """

        syc_name = "AnalysisControl"
        child_names = ["global_stabilization", "apip", "unmapped_value_options"]

        class global_stabilization(Group):
            """
            'global_stabilization' child of 'analysis_control' object
            """

            syc_name = "GlobalStabilization"
            property_names_types = [
                ("option", "Option", "String"),
                ("initial_iterations", "InitialIterations", "Integer"),
                ("initial_relaxation_factor", "InitialRelaxationFactor", "Real"),
                ("maximum_retained_time_steps", "MaximumRetainedTimeSteps", "Integer"),
                ("maximum_retained_iterations", "MaximumRetainedIterations", "Integer"),
                ("diagnostics_level", "DiagnosticsLevel", "Integer"),
                ("weight_option", "WeightOption", "String"),
                ("qr_tol_this_step", "QRTolThisStep", "Real"),
                ("qr_tol_old_steps", "QRTolOldSteps", "Real"),
                ("qr_solver", "QRSolver", "String"),
            ]

            @property
            def option(self) -> String:
                """'option' property of 'analysis_control' object"""
                return self.get_property_state("option")

            @option.setter
            def option(self, value: String):
                self.set_property_state("option", value)

            @property
            def initial_iterations(self) -> Integer:
                """'initial_iterations' property of 'analysis_control' object"""
                return self.get_property_state("initial_iterations")

            @initial_iterations.setter
            def initial_iterations(self, value: Integer):
                self.set_property_state("initial_iterations", value)

            @property
            def initial_relaxation_factor(self) -> Real:
                """'initial_relaxation_factor' property of 'analysis_control' object"""
                return self.get_property_state("initial_relaxation_factor")

            @initial_relaxation_factor.setter
            def initial_relaxation_factor(self, value: Real):
                self.set_property_state("initial_relaxation_factor", value)

            @property
            def maximum_retained_time_steps(self) -> Integer:
                """'maximum_retained_time_steps' property of 'analysis_control' object"""
                return self.get_property_state("maximum_retained_time_steps")

            @maximum_retained_time_steps.setter
            def maximum_retained_time_steps(self, value: Integer):
                self.set_property_state("maximum_retained_time_steps", value)

            @property
            def maximum_retained_iterations(self) -> Integer:
                """'maximum_retained_iterations' property of 'analysis_control' object"""
                return self.get_property_state("maximum_retained_iterations")

            @maximum_retained_iterations.setter
            def maximum_retained_iterations(self, value: Integer):
                self.set_property_state("maximum_retained_iterations", value)

            @property
            def diagnostics_level(self) -> Integer:
                """'diagnostics_level' property of 'analysis_control' object"""
                return self.get_property_state("diagnostics_level")

            @diagnostics_level.setter
            def diagnostics_level(self, value: Integer):
                self.set_property_state("diagnostics_level", value)

            @property
            def weight_option(self) -> String:
                """'weight_option' property of 'analysis_control' object"""
                return self.get_property_state("weight_option")

            @weight_option.setter
            def weight_option(self, value: String):
                self.set_property_state("weight_option", value)

            @property
            def qr_tol_this_step(self) -> Real:
                """'qr_tol_this_step' property of 'analysis_control' object"""
                return self.get_property_state("qr_tol_this_step")

            @qr_tol_this_step.setter
            def qr_tol_this_step(self, value: Real):
                self.set_property_state("qr_tol_this_step", value)

            @property
            def qr_tol_old_steps(self) -> Real:
                """'qr_tol_old_steps' property of 'analysis_control' object"""
                return self.get_property_state("qr_tol_old_steps")

            @qr_tol_old_steps.setter
            def qr_tol_old_steps(self, value: Real):
                self.set_property_state("qr_tol_old_steps", value)

            @property
            def qr_solver(self) -> String:
                """'qr_solver' property of 'analysis_control' object"""
                return self.get_property_state("qr_solver")

            @qr_solver.setter
            def qr_solver(self, value: String):
                self.set_property_state("qr_solver", value)

        class apip(Group):
            """
            'apip' child of 'analysis_control' object
            """

            syc_name = "Apip"
            property_names_types = [
                ("debug", "Debug", "Boolean"),
                ("disable", "Disable", "Boolean"),
            ]

            @property
            def debug(self) -> Boolean:
                """'debug' property of 'analysis_control' object"""
                return self.get_property_state("debug")

            @debug.setter
            def debug(self, value: Boolean):
                self.set_property_state("debug", value)

            @property
            def disable(self) -> Boolean:
                """'disable' property of 'analysis_control' object"""
                return self.get_property_state("disable")

            @disable.setter
            def disable(self, value: Boolean):
                self.set_property_state("disable", value)

        class unmapped_value_options(Group):
            """
            'unmapped_value_options' child of 'analysis_control' object
            """

            syc_name = "UnmappedValueOptions"
            property_names_types = [
                ("matrix_verbosity", "MatrixVerbosity", "Integer"),
                ("solver_verbosity", "SolverVerbosity", "Integer"),
                ("solver", "Solver", "String"),
                ("solver_relative_tolerance", "SolverRelativeTolerance", "Real"),
                ("solver_max_iterations", "SolverMaxIterations", "Integer"),
                (
                    "solver_max_search_directions",
                    "SolverMaxSearchDirections",
                    "Integer",
                ),
                ("preconditioner", "Preconditioner", "String"),
                ("ilut_tau", "IlutTau", "Real"),
                ("ilut_max_fill", "IlutMaxFill", "Integer"),
                ("ilut_pivot_tol", "IlutPivotTol", "Real"),
                ("face_filter_tolerance", "FaceFilterTolerance", "Real"),
                ("rbf_shape_parameter", "RbfShapeParameter", "Real"),
                ("rbf_linear_correction", "RbfLinearCorrection", "Boolean"),
                ("rbf_colinearity_tolerance", "RbfColinearityTolerance", "Real"),
            ]

            @property
            def matrix_verbosity(self) -> Integer:
                """'matrix_verbosity' property of 'analysis_control' object"""
                return self.get_property_state("matrix_verbosity")

            @matrix_verbosity.setter
            def matrix_verbosity(self, value: Integer):
                self.set_property_state("matrix_verbosity", value)

            @property
            def solver_verbosity(self) -> Integer:
                """'solver_verbosity' property of 'analysis_control' object"""
                return self.get_property_state("solver_verbosity")

            @solver_verbosity.setter
            def solver_verbosity(self, value: Integer):
                self.set_property_state("solver_verbosity", value)

            @property
            def solver(self) -> String:
                """'solver' property of 'analysis_control' object"""
                return self.get_property_state("solver")

            @solver.setter
            def solver(self, value: String):
                self.set_property_state("solver", value)

            @property
            def solver_relative_tolerance(self) -> Real:
                """'solver_relative_tolerance' property of 'analysis_control' object"""
                return self.get_property_state("solver_relative_tolerance")

            @solver_relative_tolerance.setter
            def solver_relative_tolerance(self, value: Real):
                self.set_property_state("solver_relative_tolerance", value)

            @property
            def solver_max_iterations(self) -> Integer:
                """'solver_max_iterations' property of 'analysis_control' object"""
                return self.get_property_state("solver_max_iterations")

            @solver_max_iterations.setter
            def solver_max_iterations(self, value: Integer):
                self.set_property_state("solver_max_iterations", value)

            @property
            def solver_max_search_directions(self) -> Integer:
                """'solver_max_search_directions' property of 'analysis_control' object"""
                return self.get_property_state("solver_max_search_directions")

            @solver_max_search_directions.setter
            def solver_max_search_directions(self, value: Integer):
                self.set_property_state("solver_max_search_directions", value)

            @property
            def preconditioner(self) -> String:
                """'preconditioner' property of 'analysis_control' object"""
                return self.get_property_state("preconditioner")

            @preconditioner.setter
            def preconditioner(self, value: String):
                self.set_property_state("preconditioner", value)

            @property
            def ilut_tau(self) -> Real:
                """'ilut_tau' property of 'analysis_control' object"""
                return self.get_property_state("ilut_tau")

            @ilut_tau.setter
            def ilut_tau(self, value: Real):
                self.set_property_state("ilut_tau", value)

            @property
            def ilut_max_fill(self) -> Integer:
                """'ilut_max_fill' property of 'analysis_control' object"""
                return self.get_property_state("ilut_max_fill")

            @ilut_max_fill.setter
            def ilut_max_fill(self, value: Integer):
                self.set_property_state("ilut_max_fill", value)

            @property
            def ilut_pivot_tol(self) -> Real:
                """'ilut_pivot_tol' property of 'analysis_control' object"""
                return self.get_property_state("ilut_pivot_tol")

            @ilut_pivot_tol.setter
            def ilut_pivot_tol(self, value: Real):
                self.set_property_state("ilut_pivot_tol", value)

            @property
            def face_filter_tolerance(self) -> Real:
                """'face_filter_tolerance' property of 'analysis_control' object"""
                return self.get_property_state("face_filter_tolerance")

            @face_filter_tolerance.setter
            def face_filter_tolerance(self, value: Real):
                self.set_property_state("face_filter_tolerance", value)

            @property
            def rbf_shape_parameter(self) -> Real:
                """'rbf_shape_parameter' property of 'analysis_control' object"""
                return self.get_property_state("rbf_shape_parameter")

            @rbf_shape_parameter.setter
            def rbf_shape_parameter(self, value: Real):
                self.set_property_state("rbf_shape_parameter", value)

            @property
            def rbf_linear_correction(self) -> Boolean:
                """'rbf_linear_correction' property of 'analysis_control' object"""
                return self.get_property_state("rbf_linear_correction")

            @rbf_linear_correction.setter
            def rbf_linear_correction(self, value: Boolean):
                self.set_property_state("rbf_linear_correction", value)

            @property
            def rbf_colinearity_tolerance(self) -> Real:
                """'rbf_colinearity_tolerance' property of 'analysis_control' object"""
                return self.get_property_state("rbf_colinearity_tolerance")

            @rbf_colinearity_tolerance.setter
            def rbf_colinearity_tolerance(self, value: Real):
                self.set_property_state("rbf_colinearity_tolerance", value)

        property_names_types = [
            ("analysis_type", "AnalysisType", "String"),
            ("optimize_if_one_way", "OptimizeIfOneWay", "Boolean"),
            ("allow_simultaneous_update", "AllowSimultaneousUpdate", "Boolean"),
            ("simultaneous_participants", "SimultaneousParticipants", "String"),
            ("partitioning_algorithm", "PartitioningAlgorithm", "String"),
            ("allow_iterations_only_mode", "AllowIterationsOnlyMode", "Boolean"),
            ("target_initialization_option", "TargetInitializationOption", "String"),
            ("fluent_region_update_at_step", "FluentRegionUpdateAtStep", "Boolean"),
            ("mesh_import_on_initialization", "MeshImportOnInitialization", "Boolean"),
            ("import_all_regions", "ImportAllRegions", "Boolean"),
            ("bypass_fluent_adapter", "BypassFluentAdapter", "Boolean"),
            (
                "variable_to_expression_transfer",
                "VariableToExpressionTransfer",
                "Boolean",
            ),
            ("update_mapping_weights", "UpdateMappingWeights", "String"),
            ("rotate_follower_forces", "RotateFollowerForces", "String"),
            (
                "solve_incremental_displacement_first",
                "SolveIncrementalDisplacementFirst",
                "Boolean",
            ),
            ("write_scs_file", "WriteScsFile", "Boolean"),
            ("check_for_input_files_changes", "CheckForInputFilesChanges", "String"),
        ]

        @property
        def analysis_type(self) -> String:
            """'analysis_type' property of 'root' object"""
            return self.get_property_state("analysis_type")

        @analysis_type.setter
        def analysis_type(self, value: String):
            self.set_property_state("analysis_type", value)

        @property
        def optimize_if_one_way(self) -> Boolean:
            """'optimize_if_one_way' property of 'root' object"""
            return self.get_property_state("optimize_if_one_way")

        @optimize_if_one_way.setter
        def optimize_if_one_way(self, value: Boolean):
            self.set_property_state("optimize_if_one_way", value)

        @property
        def allow_simultaneous_update(self) -> Boolean:
            """'allow_simultaneous_update' property of 'root' object"""
            return self.get_property_state("allow_simultaneous_update")

        @allow_simultaneous_update.setter
        def allow_simultaneous_update(self, value: Boolean):
            self.set_property_state("allow_simultaneous_update", value)

        @property
        def simultaneous_participants(self) -> String:
            """'simultaneous_participants' property of 'root' object"""
            return self.get_property_state("simultaneous_participants")

        @simultaneous_participants.setter
        def simultaneous_participants(self, value: String):
            self.set_property_state("simultaneous_participants", value)

        @property
        def partitioning_algorithm(self) -> String:
            """'partitioning_algorithm' property of 'root' object"""
            return self.get_property_state("partitioning_algorithm")

        @partitioning_algorithm.setter
        def partitioning_algorithm(self, value: String):
            self.set_property_state("partitioning_algorithm", value)

        @property
        def allow_iterations_only_mode(self) -> Boolean:
            """'allow_iterations_only_mode' property of 'root' object"""
            return self.get_property_state("allow_iterations_only_mode")

        @allow_iterations_only_mode.setter
        def allow_iterations_only_mode(self, value: Boolean):
            self.set_property_state("allow_iterations_only_mode", value)

        @property
        def target_initialization_option(self) -> String:
            """'target_initialization_option' property of 'root' object"""
            return self.get_property_state("target_initialization_option")

        @target_initialization_option.setter
        def target_initialization_option(self, value: String):
            self.set_property_state("target_initialization_option", value)

        @property
        def fluent_region_update_at_step(self) -> Boolean:
            """'fluent_region_update_at_step' property of 'root' object"""
            return self.get_property_state("fluent_region_update_at_step")

        @fluent_region_update_at_step.setter
        def fluent_region_update_at_step(self, value: Boolean):
            self.set_property_state("fluent_region_update_at_step", value)

        @property
        def mesh_import_on_initialization(self) -> Boolean:
            """'mesh_import_on_initialization' property of 'root' object"""
            return self.get_property_state("mesh_import_on_initialization")

        @mesh_import_on_initialization.setter
        def mesh_import_on_initialization(self, value: Boolean):
            self.set_property_state("mesh_import_on_initialization", value)

        @property
        def import_all_regions(self) -> Boolean:
            """'import_all_regions' property of 'root' object"""
            return self.get_property_state("import_all_regions")

        @import_all_regions.setter
        def import_all_regions(self, value: Boolean):
            self.set_property_state("import_all_regions", value)

        @property
        def bypass_fluent_adapter(self) -> Boolean:
            """'bypass_fluent_adapter' property of 'root' object"""
            return self.get_property_state("bypass_fluent_adapter")

        @bypass_fluent_adapter.setter
        def bypass_fluent_adapter(self, value: Boolean):
            self.set_property_state("bypass_fluent_adapter", value)

        @property
        def variable_to_expression_transfer(self) -> Boolean:
            """'variable_to_expression_transfer' property of 'root' object"""
            return self.get_property_state("variable_to_expression_transfer")

        @variable_to_expression_transfer.setter
        def variable_to_expression_transfer(self, value: Boolean):
            self.set_property_state("variable_to_expression_transfer", value)

        @property
        def update_mapping_weights(self) -> String:
            """'update_mapping_weights' property of 'root' object"""
            return self.get_property_state("update_mapping_weights")

        @update_mapping_weights.setter
        def update_mapping_weights(self, value: String):
            self.set_property_state("update_mapping_weights", value)

        @property
        def rotate_follower_forces(self) -> String:
            """'rotate_follower_forces' property of 'root' object"""
            return self.get_property_state("rotate_follower_forces")

        @rotate_follower_forces.setter
        def rotate_follower_forces(self, value: String):
            self.set_property_state("rotate_follower_forces", value)

        @property
        def solve_incremental_displacement_first(self) -> Boolean:
            """'solve_incremental_displacement_first' property of 'root' object"""
            return self.get_property_state("solve_incremental_displacement_first")

        @solve_incremental_displacement_first.setter
        def solve_incremental_displacement_first(self, value: Boolean):
            self.set_property_state("solve_incremental_displacement_first", value)

        @property
        def write_scs_file(self) -> Boolean:
            """'write_scs_file' property of 'root' object"""
            return self.get_property_state("write_scs_file")

        @write_scs_file.setter
        def write_scs_file(self, value: Boolean):
            self.set_property_state("write_scs_file", value)

        @property
        def check_for_input_files_changes(self) -> String:
            """'check_for_input_files_changes' property of 'root' object"""
            return self.get_property_state("check_for_input_files_changes")

        @check_for_input_files_changes.setter
        def check_for_input_files_changes(self, value: String):
            self.set_property_state("check_for_input_files_changes", value)

    class coupling_interface(NamedObject):
        """
        'coupling_interface' child of 'root' object
        """

        syc_name = "CouplingInterface"

        class child_object_type(Group):
            """
            'child_object_type' child of 'coupling_interface' object
            """

            syc_name = "child_object_type"
            child_names = ["side", "data_transfer", "mapping_control"]

            class side(NamedObject):
                """
                'side' child of 'child_object_type' object
                """

                syc_name = "Side"

                class child_object_type(Group):
                    """
                    'child_object_type' child of 'side' object
                    """

                    syc_name = "child_object_type"
                    property_names_types = [
                        ("coupling_participant", "CouplingParticipant", "String"),
                        ("region_list", "RegionList", "StringList"),
                        ("reference_frame", "ReferenceFrame", "String"),
                        ("instancing", "Instancing", "String"),
                    ]

                    @property
                    def coupling_participant(self) -> String:
                        """'coupling_participant' property of 'side' object"""
                        return self.get_property_state("coupling_participant")

                    @coupling_participant.setter
                    def coupling_participant(self, value: String):
                        self.set_property_state("coupling_participant", value)

                    @property
                    def region_list(self) -> StringList:
                        """'region_list' property of 'side' object"""
                        return self.get_property_state("region_list")

                    @region_list.setter
                    def region_list(self, value: StringList):
                        self.set_property_state("region_list", value)

                    @property
                    def reference_frame(self) -> String:
                        """'reference_frame' property of 'side' object"""
                        return self.get_property_state("reference_frame")

                    @reference_frame.setter
                    def reference_frame(self, value: String):
                        self.set_property_state("reference_frame", value)

                    @property
                    def instancing(self) -> String:
                        """'instancing' property of 'side' object"""
                        return self.get_property_state("instancing")

                    @instancing.setter
                    def instancing(self, value: String):
                        self.set_property_state("instancing", value)

            class data_transfer(NamedObject):
                """
                'data_transfer' child of 'child_object_type' object
                """

                syc_name = "DataTransfer"

                class child_object_type(Group):
                    """
                    'child_object_type' child of 'data_transfer' object
                    """

                    syc_name = "child_object_type"
                    child_names = ["stabilization"]

                    class stabilization(Group):
                        """
                        'stabilization' child of 'child_object_type' object
                        """

                        syc_name = "Stabilization"
                        property_names_types = [
                            ("option", "Option", "String"),
                            (
                                "couple_with_global_stabilization",
                                "CoupleWithGlobalStabilization",
                                "Boolean",
                            ),
                            ("initial_iterations", "InitialIterations", "Integer"),
                            (
                                "initial_relaxation_factor",
                                "InitialRelaxationFactor",
                                "Real",
                            ),
                            (
                                "maximum_retained_time_steps",
                                "MaximumRetainedTimeSteps",
                                "Integer",
                            ),
                            (
                                "maximum_retained_iterations",
                                "MaximumRetainedIterations",
                                "Integer",
                            ),
                            ("weight_factor", "WeightFactor", "Real"),
                            ("diagnostics_level", "DiagnosticsLevel", "Integer"),
                            ("weight_option", "WeightOption", "String"),
                            ("qr_tol_this_step", "QRTolThisStep", "Real"),
                            ("qr_tol_old_steps", "QRTolOldSteps", "Real"),
                            (
                                "time_step_initialization_option",
                                "TimeStepInitializationOption",
                                "String",
                            ),
                        ]

                        @property
                        def option(self) -> String:
                            """'option' property of 'child_object_type' object"""
                            return self.get_property_state("option")

                        @option.setter
                        def option(self, value: String):
                            self.set_property_state("option", value)

                        @property
                        def couple_with_global_stabilization(self) -> Boolean:
                            """'couple_with_global_stabilization' property of 'child_object_type' object"""
                            return self.get_property_state(
                                "couple_with_global_stabilization"
                            )

                        @couple_with_global_stabilization.setter
                        def couple_with_global_stabilization(self, value: Boolean):
                            self.set_property_state(
                                "couple_with_global_stabilization", value
                            )

                        @property
                        def initial_iterations(self) -> Integer:
                            """'initial_iterations' property of 'child_object_type' object"""
                            return self.get_property_state("initial_iterations")

                        @initial_iterations.setter
                        def initial_iterations(self, value: Integer):
                            self.set_property_state("initial_iterations", value)

                        @property
                        def initial_relaxation_factor(self) -> Real:
                            """'initial_relaxation_factor' property of 'child_object_type' object"""
                            return self.get_property_state("initial_relaxation_factor")

                        @initial_relaxation_factor.setter
                        def initial_relaxation_factor(self, value: Real):
                            self.set_property_state("initial_relaxation_factor", value)

                        @property
                        def maximum_retained_time_steps(self) -> Integer:
                            """'maximum_retained_time_steps' property of 'child_object_type' object"""
                            return self.get_property_state(
                                "maximum_retained_time_steps"
                            )

                        @maximum_retained_time_steps.setter
                        def maximum_retained_time_steps(self, value: Integer):
                            self.set_property_state(
                                "maximum_retained_time_steps", value
                            )

                        @property
                        def maximum_retained_iterations(self) -> Integer:
                            """'maximum_retained_iterations' property of 'child_object_type' object"""
                            return self.get_property_state(
                                "maximum_retained_iterations"
                            )

                        @maximum_retained_iterations.setter
                        def maximum_retained_iterations(self, value: Integer):
                            self.set_property_state(
                                "maximum_retained_iterations", value
                            )

                        @property
                        def weight_factor(self) -> Real:
                            """'weight_factor' property of 'child_object_type' object"""
                            return self.get_property_state("weight_factor")

                        @weight_factor.setter
                        def weight_factor(self, value: Real):
                            self.set_property_state("weight_factor", value)

                        @property
                        def diagnostics_level(self) -> Integer:
                            """'diagnostics_level' property of 'child_object_type' object"""
                            return self.get_property_state("diagnostics_level")

                        @diagnostics_level.setter
                        def diagnostics_level(self, value: Integer):
                            self.set_property_state("diagnostics_level", value)

                        @property
                        def weight_option(self) -> String:
                            """'weight_option' property of 'child_object_type' object"""
                            return self.get_property_state("weight_option")

                        @weight_option.setter
                        def weight_option(self, value: String):
                            self.set_property_state("weight_option", value)

                        @property
                        def qr_tol_this_step(self) -> Real:
                            """'qr_tol_this_step' property of 'child_object_type' object"""
                            return self.get_property_state("qr_tol_this_step")

                        @qr_tol_this_step.setter
                        def qr_tol_this_step(self, value: Real):
                            self.set_property_state("qr_tol_this_step", value)

                        @property
                        def qr_tol_old_steps(self) -> Real:
                            """'qr_tol_old_steps' property of 'child_object_type' object"""
                            return self.get_property_state("qr_tol_old_steps")

                        @qr_tol_old_steps.setter
                        def qr_tol_old_steps(self, value: Real):
                            self.set_property_state("qr_tol_old_steps", value)

                        @property
                        def time_step_initialization_option(self) -> String:
                            """'time_step_initialization_option' property of 'child_object_type' object"""
                            return self.get_property_state(
                                "time_step_initialization_option"
                            )

                        @time_step_initialization_option.setter
                        def time_step_initialization_option(self, value: String):
                            self.set_property_state(
                                "time_step_initialization_option", value
                            )

                    property_names_types = [
                        ("display_name", "DisplayName", "String"),
                        ("suppress", "Suppress", "Boolean"),
                        ("target_side", "TargetSide", "String"),
                        ("option", "Option", "String"),
                        ("source_variable", "SourceVariable", "String"),
                        ("target_variable", "TargetVariable", "String"),
                        ("value", "Value", "Real"),
                        ("ramping_option", "RampingOption", "String"),
                        ("relaxation_factor", "RelaxationFactor", "Real"),
                        ("convergence_target", "ConvergenceTarget", "Real"),
                        ("mapping_type", "MappingType", "String"),
                        ("unmapped_value_option", "UnmappedValueOption", "String"),
                        (
                            "time_step_initialization_option",
                            "TimeStepInitializationOption",
                            "String",
                        ),
                    ]

                    @property
                    def display_name(self) -> String:
                        """'display_name' property of 'data_transfer' object"""
                        return self.get_property_state("display_name")

                    @display_name.setter
                    def display_name(self, value: String):
                        self.set_property_state("display_name", value)

                    @property
                    def suppress(self) -> Boolean:
                        """'suppress' property of 'data_transfer' object"""
                        return self.get_property_state("suppress")

                    @suppress.setter
                    def suppress(self, value: Boolean):
                        self.set_property_state("suppress", value)

                    @property
                    def target_side(self) -> String:
                        """'target_side' property of 'data_transfer' object"""
                        return self.get_property_state("target_side")

                    @target_side.setter
                    def target_side(self, value: String):
                        self.set_property_state("target_side", value)

                    @property
                    def option(self) -> String:
                        """'option' property of 'data_transfer' object"""
                        return self.get_property_state("option")

                    @option.setter
                    def option(self, value: String):
                        self.set_property_state("option", value)

                    @property
                    def source_variable(self) -> String:
                        """'source_variable' property of 'data_transfer' object"""
                        return self.get_property_state("source_variable")

                    @source_variable.setter
                    def source_variable(self, value: String):
                        self.set_property_state("source_variable", value)

                    @property
                    def target_variable(self) -> String:
                        """'target_variable' property of 'data_transfer' object"""
                        return self.get_property_state("target_variable")

                    @target_variable.setter
                    def target_variable(self, value: String):
                        self.set_property_state("target_variable", value)

                    @property
                    def value(self) -> Real:
                        """'value' property of 'data_transfer' object"""
                        return self.get_property_state("value")

                    @value.setter
                    def value(self, value: Real):
                        self.set_property_state("value", value)

                    @property
                    def ramping_option(self) -> String:
                        """'ramping_option' property of 'data_transfer' object"""
                        return self.get_property_state("ramping_option")

                    @ramping_option.setter
                    def ramping_option(self, value: String):
                        self.set_property_state("ramping_option", value)

                    @property
                    def relaxation_factor(self) -> Real:
                        """'relaxation_factor' property of 'data_transfer' object"""
                        return self.get_property_state("relaxation_factor")

                    @relaxation_factor.setter
                    def relaxation_factor(self, value: Real):
                        self.set_property_state("relaxation_factor", value)

                    @property
                    def convergence_target(self) -> Real:
                        """'convergence_target' property of 'data_transfer' object"""
                        return self.get_property_state("convergence_target")

                    @convergence_target.setter
                    def convergence_target(self, value: Real):
                        self.set_property_state("convergence_target", value)

                    @property
                    def mapping_type(self) -> String:
                        """'mapping_type' property of 'data_transfer' object"""
                        return self.get_property_state("mapping_type")

                    @mapping_type.setter
                    def mapping_type(self, value: String):
                        self.set_property_state("mapping_type", value)

                    @property
                    def unmapped_value_option(self) -> String:
                        """'unmapped_value_option' property of 'data_transfer' object"""
                        return self.get_property_state("unmapped_value_option")

                    @unmapped_value_option.setter
                    def unmapped_value_option(self, value: String):
                        self.set_property_state("unmapped_value_option", value)

                    @property
                    def time_step_initialization_option(self) -> String:
                        """'time_step_initialization_option' property of 'data_transfer' object"""
                        return self.get_property_state(
                            "time_step_initialization_option"
                        )

                    @time_step_initialization_option.setter
                    def time_step_initialization_option(self, value: String):
                        self.set_property_state(
                            "time_step_initialization_option", value
                        )

            class mapping_control(Group):
                """
                'mapping_control' child of 'child_object_type' object
                """

                syc_name = "MappingControl"
                property_names_types = [
                    ("stop_if_poor_intersection", "StopIfPoorIntersection", "Boolean"),
                    (
                        "poor_intersection_threshold",
                        "PoorIntersectionThreshold",
                        "Real",
                    ),
                    ("face_alignment", "FaceAlignment", "String"),
                    ("absolute_gap_tolerance", "AbsoluteGapTolerance", "Real"),
                    ("relative_gap_tolerance", "RelativeGapTolerance", "Real"),
                    ("small_weight_tolerance", "SmallWeightTolerance", "Real"),
                    ("corner_tolerance", "CornerTolerance", "Real"),
                    ("halo_tolerance", "HaloTolerance", "Real"),
                    (
                        "conservative_reciprocity_factor",
                        "ConservativeReciprocityFactor",
                        "Real",
                    ),
                    (
                        "profile_preserving_reciprocity_factor",
                        "ProfilePreservingReciprocityFactor",
                        "Real",
                    ),
                    ("conservative_intensive", "ConservativeIntensive", "String"),
                    ("preserve_normal", "PreserveNormal", "String"),
                    (
                        "conservation_fix_tolerance_volume",
                        "ConservationFixToleranceVolume",
                        "Real",
                    ),
                    ("rbf_option", "RBFOption", "String"),
                    ("rbf_shape_parameter", "RBFShapeParameter", "Real"),
                    ("rbf_linear_correction", "RBFLinearCorrection", "Boolean"),
                    ("rbf_clipping_scale", "RBFClippingScale", "Real"),
                ]

                @property
                def stop_if_poor_intersection(self) -> Boolean:
                    """'stop_if_poor_intersection' property of 'child_object_type' object"""
                    return self.get_property_state("stop_if_poor_intersection")

                @stop_if_poor_intersection.setter
                def stop_if_poor_intersection(self, value: Boolean):
                    self.set_property_state("stop_if_poor_intersection", value)

                @property
                def poor_intersection_threshold(self) -> Real:
                    """'poor_intersection_threshold' property of 'child_object_type' object"""
                    return self.get_property_state("poor_intersection_threshold")

                @poor_intersection_threshold.setter
                def poor_intersection_threshold(self, value: Real):
                    self.set_property_state("poor_intersection_threshold", value)

                @property
                def face_alignment(self) -> String:
                    """'face_alignment' property of 'child_object_type' object"""
                    return self.get_property_state("face_alignment")

                @face_alignment.setter
                def face_alignment(self, value: String):
                    self.set_property_state("face_alignment", value)

                @property
                def absolute_gap_tolerance(self) -> Real:
                    """'absolute_gap_tolerance' property of 'child_object_type' object"""
                    return self.get_property_state("absolute_gap_tolerance")

                @absolute_gap_tolerance.setter
                def absolute_gap_tolerance(self, value: Real):
                    self.set_property_state("absolute_gap_tolerance", value)

                @property
                def relative_gap_tolerance(self) -> Real:
                    """'relative_gap_tolerance' property of 'child_object_type' object"""
                    return self.get_property_state("relative_gap_tolerance")

                @relative_gap_tolerance.setter
                def relative_gap_tolerance(self, value: Real):
                    self.set_property_state("relative_gap_tolerance", value)

                @property
                def small_weight_tolerance(self) -> Real:
                    """'small_weight_tolerance' property of 'child_object_type' object"""
                    return self.get_property_state("small_weight_tolerance")

                @small_weight_tolerance.setter
                def small_weight_tolerance(self, value: Real):
                    self.set_property_state("small_weight_tolerance", value)

                @property
                def corner_tolerance(self) -> Real:
                    """'corner_tolerance' property of 'child_object_type' object"""
                    return self.get_property_state("corner_tolerance")

                @corner_tolerance.setter
                def corner_tolerance(self, value: Real):
                    self.set_property_state("corner_tolerance", value)

                @property
                def halo_tolerance(self) -> Real:
                    """'halo_tolerance' property of 'child_object_type' object"""
                    return self.get_property_state("halo_tolerance")

                @halo_tolerance.setter
                def halo_tolerance(self, value: Real):
                    self.set_property_state("halo_tolerance", value)

                @property
                def conservative_reciprocity_factor(self) -> Real:
                    """'conservative_reciprocity_factor' property of 'child_object_type' object"""
                    return self.get_property_state("conservative_reciprocity_factor")

                @conservative_reciprocity_factor.setter
                def conservative_reciprocity_factor(self, value: Real):
                    self.set_property_state("conservative_reciprocity_factor", value)

                @property
                def profile_preserving_reciprocity_factor(self) -> Real:
                    """'profile_preserving_reciprocity_factor' property of 'child_object_type' object"""
                    return self.get_property_state(
                        "profile_preserving_reciprocity_factor"
                    )

                @profile_preserving_reciprocity_factor.setter
                def profile_preserving_reciprocity_factor(self, value: Real):
                    self.set_property_state(
                        "profile_preserving_reciprocity_factor", value
                    )

                @property
                def conservative_intensive(self) -> String:
                    """'conservative_intensive' property of 'child_object_type' object"""
                    return self.get_property_state("conservative_intensive")

                @conservative_intensive.setter
                def conservative_intensive(self, value: String):
                    self.set_property_state("conservative_intensive", value)

                @property
                def preserve_normal(self) -> String:
                    """'preserve_normal' property of 'child_object_type' object"""
                    return self.get_property_state("preserve_normal")

                @preserve_normal.setter
                def preserve_normal(self, value: String):
                    self.set_property_state("preserve_normal", value)

                @property
                def conservation_fix_tolerance_volume(self) -> Real:
                    """'conservation_fix_tolerance_volume' property of 'child_object_type' object"""
                    return self.get_property_state("conservation_fix_tolerance_volume")

                @conservation_fix_tolerance_volume.setter
                def conservation_fix_tolerance_volume(self, value: Real):
                    self.set_property_state("conservation_fix_tolerance_volume", value)

                @property
                def rbf_option(self) -> String:
                    """'rbf_option' property of 'child_object_type' object"""
                    return self.get_property_state("rbf_option")

                @rbf_option.setter
                def rbf_option(self, value: String):
                    self.set_property_state("rbf_option", value)

                @property
                def rbf_shape_parameter(self) -> Real:
                    """'rbf_shape_parameter' property of 'child_object_type' object"""
                    return self.get_property_state("rbf_shape_parameter")

                @rbf_shape_parameter.setter
                def rbf_shape_parameter(self, value: Real):
                    self.set_property_state("rbf_shape_parameter", value)

                @property
                def rbf_linear_correction(self) -> Boolean:
                    """'rbf_linear_correction' property of 'child_object_type' object"""
                    return self.get_property_state("rbf_linear_correction")

                @rbf_linear_correction.setter
                def rbf_linear_correction(self, value: Boolean):
                    self.set_property_state("rbf_linear_correction", value)

                @property
                def rbf_clipping_scale(self) -> Real:
                    """'rbf_clipping_scale' property of 'child_object_type' object"""
                    return self.get_property_state("rbf_clipping_scale")

                @rbf_clipping_scale.setter
                def rbf_clipping_scale(self, value: Real):
                    self.set_property_state("rbf_clipping_scale", value)

            property_names_types = [("display_name", "DisplayName", "String")]

            @property
            def display_name(self) -> String:
                """'display_name' property of 'coupling_interface' object"""
                return self.get_property_state("display_name")

            @display_name.setter
            def display_name(self, value: String):
                self.set_property_state("display_name", value)

    class solution_control(Group):
        """
        'solution_control' child of 'root' object
        """

        syc_name = "SolutionControl"
        child_names = ["available_ports"]

        class available_ports(Group):
            """
            'available_ports' child of 'solution_control' object
            """

            syc_name = "AvailablePorts"
            property_names_types = [
                ("option", "Option", "String"),
                ("range", "Range", "String"),
            ]

            @property
            def option(self) -> String:
                """'option' property of 'solution_control' object"""
                return self.get_property_state("option")

            @option.setter
            def option(self, value: String):
                self.set_property_state("option", value)

            @property
            def range(self) -> String:
                """'range' property of 'solution_control' object"""
                return self.get_property_state("range")

            @range.setter
            def range(self, value: String):
                self.set_property_state("range", value)

        property_names_types = [
            ("duration_option", "DurationOption", "String"),
            ("end_time", "EndTime", "Real"),
            ("number_of_steps", "NumberOfSteps", "Integer"),
            ("time_step_size", "TimeStepSize", "Real"),
            ("minimum_iterations", "MinimumIterations", "Integer"),
            ("maximum_iterations", "MaximumIterations", "Integer"),
        ]

        @property
        def duration_option(self) -> String:
            """'duration_option' property of 'root' object"""
            return self.get_property_state("duration_option")

        @duration_option.setter
        def duration_option(self, value: String):
            self.set_property_state("duration_option", value)

        @property
        def end_time(self) -> Real:
            """'end_time' property of 'root' object"""
            return self.get_property_state("end_time")

        @end_time.setter
        def end_time(self, value: Real):
            self.set_property_state("end_time", value)

        @property
        def number_of_steps(self) -> Integer:
            """'number_of_steps' property of 'root' object"""
            return self.get_property_state("number_of_steps")

        @number_of_steps.setter
        def number_of_steps(self, value: Integer):
            self.set_property_state("number_of_steps", value)

        @property
        def time_step_size(self) -> Real:
            """'time_step_size' property of 'root' object"""
            return self.get_property_state("time_step_size")

        @time_step_size.setter
        def time_step_size(self, value: Real):
            self.set_property_state("time_step_size", value)

        @property
        def minimum_iterations(self) -> Integer:
            """'minimum_iterations' property of 'root' object"""
            return self.get_property_state("minimum_iterations")

        @minimum_iterations.setter
        def minimum_iterations(self, value: Integer):
            self.set_property_state("minimum_iterations", value)

        @property
        def maximum_iterations(self) -> Integer:
            """'maximum_iterations' property of 'root' object"""
            return self.get_property_state("maximum_iterations")

        @maximum_iterations.setter
        def maximum_iterations(self, value: Integer):
            self.set_property_state("maximum_iterations", value)

    class output_control(Group):
        """
        'output_control' child of 'root' object
        """

        syc_name = "OutputControl"
        child_names = ["results", "ascii_output"]

        class results(Group):
            """
            'results' child of 'output_control' object
            """

            syc_name = "Results"
            child_names = ["type"]

            class type(Group):
                """
                'type' child of 'results' object
                """

                syc_name = "Type"
                property_names_types = [
                    ("option", "Option", "String"),
                    ("binary_format", "BinaryFormat", "Boolean"),
                ]

                @property
                def option(self) -> String:
                    """'option' property of 'results' object"""
                    return self.get_property_state("option")

                @option.setter
                def option(self, value: String):
                    self.set_property_state("option", value)

                @property
                def binary_format(self) -> Boolean:
                    """'binary_format' property of 'results' object"""
                    return self.get_property_state("binary_format")

                @binary_format.setter
                def binary_format(self, value: Boolean):
                    self.set_property_state("binary_format", value)

            property_names_types = [
                ("option", "Option", "String"),
                ("include_instances", "IncludeInstances", "String"),
                ("output_frequency", "OutputFrequency", "Integer"),
            ]

            @property
            def option(self) -> String:
                """'option' property of 'output_control' object"""
                return self.get_property_state("option")

            @option.setter
            def option(self, value: String):
                self.set_property_state("option", value)

            @property
            def include_instances(self) -> String:
                """'include_instances' property of 'output_control' object"""
                return self.get_property_state("include_instances")

            @include_instances.setter
            def include_instances(self, value: String):
                self.set_property_state("include_instances", value)

            @property
            def output_frequency(self) -> Integer:
                """'output_frequency' property of 'output_control' object"""
                return self.get_property_state("output_frequency")

            @output_frequency.setter
            def output_frequency(self, value: Integer):
                self.set_property_state("output_frequency", value)

        class ascii_output(Group):
            """
            'ascii_output' child of 'output_control' object
            """

            syc_name = "AsciiOutput"
            property_names_types = [
                ("option", "Option", "String"),
                ("format", "Format", "String"),
            ]

            @property
            def option(self) -> String:
                """'option' property of 'output_control' object"""
                return self.get_property_state("option")

            @option.setter
            def option(self, value: String):
                self.set_property_state("option", value)

            @property
            def format(self) -> String:
                """'format' property of 'output_control' object"""
                return self.get_property_state("format")

            @format.setter
            def format(self, value: String):
                self.set_property_state("format", value)

        property_names_types = [
            ("option", "Option", "String"),
            ("generate_csv_chart_output", "GenerateCSVChartOutput", "Boolean"),
            ("write_initial_snapshot", "WriteInitialSnapshot", "Boolean"),
            ("transcript_precision", "TranscriptPrecision", "Integer"),
            ("write_diagnostics", "WriteDiagnostics", "Boolean"),
            ("write_weights_matrix", "WriteWeightsMatrix", "Boolean"),
            ("write_residuals", "WriteResiduals", "Boolean"),
            ("output_frequency", "OutputFrequency", "Integer"),
        ]

        @property
        def option(self) -> String:
            """'option' property of 'root' object"""
            return self.get_property_state("option")

        @option.setter
        def option(self, value: String):
            self.set_property_state("option", value)

        @property
        def generate_csv_chart_output(self) -> Boolean:
            """'generate_csv_chart_output' property of 'root' object"""
            return self.get_property_state("generate_csv_chart_output")

        @generate_csv_chart_output.setter
        def generate_csv_chart_output(self, value: Boolean):
            self.set_property_state("generate_csv_chart_output", value)

        @property
        def write_initial_snapshot(self) -> Boolean:
            """'write_initial_snapshot' property of 'root' object"""
            return self.get_property_state("write_initial_snapshot")

        @write_initial_snapshot.setter
        def write_initial_snapshot(self, value: Boolean):
            self.set_property_state("write_initial_snapshot", value)

        @property
        def transcript_precision(self) -> Integer:
            """'transcript_precision' property of 'root' object"""
            return self.get_property_state("transcript_precision")

        @transcript_precision.setter
        def transcript_precision(self, value: Integer):
            self.set_property_state("transcript_precision", value)

        @property
        def write_diagnostics(self) -> Boolean:
            """'write_diagnostics' property of 'root' object"""
            return self.get_property_state("write_diagnostics")

        @write_diagnostics.setter
        def write_diagnostics(self, value: Boolean):
            self.set_property_state("write_diagnostics", value)

        @property
        def write_weights_matrix(self) -> Boolean:
            """'write_weights_matrix' property of 'root' object"""
            return self.get_property_state("write_weights_matrix")

        @write_weights_matrix.setter
        def write_weights_matrix(self, value: Boolean):
            self.set_property_state("write_weights_matrix", value)

        @property
        def write_residuals(self) -> Boolean:
            """'write_residuals' property of 'root' object"""
            return self.get_property_state("write_residuals")

        @write_residuals.setter
        def write_residuals(self, value: Boolean):
            self.set_property_state("write_residuals", value)

        @property
        def output_frequency(self) -> Integer:
            """'output_frequency' property of 'root' object"""
            return self.get_property_state("output_frequency")

        @output_frequency.setter
        def output_frequency(self, value: Integer):
            self.set_property_state("output_frequency", value)

    command_names = [
        "add_interface",
        "add_interface_by_display_names",
        "add_data_transfer",
        "add_data_transfer_by_display_names",
        "get_region_names_for_participant",
        "add_reference_frame",
        "add_transformation",
        "delete_transformation",
        "add_participant",
        "import_system_coupling_input_file",
        "get_expression_variables",
        "add_default_transformation",
        "add_instancing",
        "get_errors",
        "add_named_expression",
        "add_expression_function",
        "reload_expression_function_modules",
    ]

    class add_interface(Command):
        """
        Adds an interface based on the participant and region names specified
        as arguments for each side of the interface. This command requires that you
        specify participants and regions using their names as described below in
        Essential Keyword Arguments.

        Cannot be run after participants have been started.

        Returns the name of the Interface created.

        Parameters
        ----------
            side_one_participant : str
                String indicating the name of the participant to be associated with
        side One of the interface.
            side_one_regions : typing.List[str]
                List specifying the name(s) of region(s) to be added to side One of
        the interface.
            side_two_participant : str
                String indicating the name of the participant to be associated with
        side Two of the interface.
            side_two_regions : typing.List[str]
                List specifying the name(s) of region(s) to be added to side Two of
        the interface.

        """

        syc_name = "AddInterface"
        argument_names = [
            "side_one_participant",
            "side_one_regions",
            "side_two_participant",
            "side_two_regions",
        ]
        essential_arguments = [
            "side_one_participant",
            "side_one_regions",
            "side_two_participant",
            "side_two_regions",
        ]

        class side_one_participant(String):
            """
            String indicating the name of the participant to be associated with
            side One of the interface.
            """

            syc_name = "SideOneParticipant"

        class side_one_regions(StringList):
            """
            List specifying the name(s) of region(s) to be added to side One of
            the interface.
            """

            syc_name = "SideOneRegions"

        class side_two_participant(String):
            """
            String indicating the name of the participant to be associated with
            side Two of the interface.
            """

            syc_name = "SideTwoParticipant"

        class side_two_regions(StringList):
            """
            List specifying the name(s) of region(s) to be added to side Two of
            the interface.
            """

            syc_name = "SideTwoRegions"

    class add_interface_by_display_names(Command):
        """
        Adds an interface based on the participant and region names specified
        as arguments for each side of the interface. This command requires that you
        specify participants and regions using their names, as described below in
        Essential Keyword Arguments.

        Cannot be run after participants have been started.

        Returns the name of the Interface created.

        Parameters
        ----------
            side_one_participant : str
                String indicating the name of the participant to be associated with
        side One of the interface.
            side_one_regions : typing.List[str]
                List specifying the name(s) of region(s) to be added to side One of
        the interface.
            side_two_participant : str
                String indicating the name of the participant to be associated with
        side Two of the interface.
            side_two_regions : typing.List[str]
                List specifying the name(s) of region(s) to be added to side Two
        of the interface.

        """

        syc_name = "AddInterfaceByDisplayNames"
        argument_names = [
            "side_one_participant",
            "side_one_regions",
            "side_two_participant",
            "side_two_regions",
        ]
        essential_arguments = [
            "side_one_participant",
            "side_one_regions",
            "side_two_participant",
            "side_two_regions",
        ]

        class side_one_participant(String):
            """
            String indicating the name of the participant to be associated with
            side One of the interface.
            """

            syc_name = "SideOneParticipant"

        class side_one_regions(StringList):
            """
            List specifying the name(s) of region(s) to be added to side One of
            the interface.
            """

            syc_name = "SideOneRegions"

        class side_two_participant(String):
            """
            String indicating the name of the participant to be associated with
            side Two of the interface.
            """

            syc_name = "SideTwoParticipant"

        class side_two_regions(StringList):
            """
            List specifying the name(s) of region(s) to be added to side Two
            of the interface.
            """

            syc_name = "SideTwoRegions"

    class add_data_transfer(Command):
        """
        Adds data transfer based on arguments that specify the interface, target
        side, and variables to be associated with each side of the interface.
        The command requires that you specify variables using their names, as
        described below in Essential Keyword Arguments. Either a variable-based or
        expression-based data transfer may be created with this command based on
        the Optional Keyword Arguments. If a variable-based data transfer argument
        is given, then no expression-based data transfer arguments can be used. If
        an expression-based data transfer argument is given, then no variable-based
        data transfer arguments can be used.

        Cannot be run after participants have been started.

        Returns the name of the Data Transfer created.

        Parameters
        ----------
            interface : str
                String indicating the name of the interface on which the data transfer
        is to be created.
            target_side : str
                String indicating the side of the interface to receive the data
        transfer variable. Possible values are 'One' or 'Two'.
            source_variable : str
                String specifying the name of the variable on the source side of
        the data transfer. Used when creating a variable-based data transfer.
        Must be combined with ??target_variable??.
            target_variable : str
                String specifying the name of the variable on the target side of
        the data transfer. Must be combined with either ??source_variable?? (when
        creating a variable-based data transfer) or with ??value??{X|Y|Z}
        (when creating an expression-based data transfer).
            value : str
                String specifying the expression to use on the source side of the data
        transfer. Used when creating an expression-based data transfer. If the
        ??target_variable?? is a vector, a vector-valued expression must be provided.
        Alternatively, ??value_x??, ??value_y??, ??value_z?? may be used to specify the
        individual components of the vector expression.
            value_x : str
                String specifying the X component of the expression to use on the
        source side of the data transfer. This may optionally be used when creating
        an expression-based data transfer if the ??target_variable?? is a vector as an
        alternative to specifying a vector-valued expression in ??value??. ??value_y?? and
        ??value_z?? are also required if ??value_x?? is used.
            value_y : str
                String specifying the Y component of the expression to use on the
        source side of the data transfer. This may optionally be used when creating
        an expression-based data transfer if the ??target_variable?? is a vector as an
        alternative to specifying a vector-valued expression in ??value??. ??value_x?? and
        ??value_z?? are also required if ??value_y?? is used.
            value_z : str
                String specifying the Z component of the expression to use on the
        source side of the data transfer. This may optionally be used when creating
        an expression-based data transfer if the ??target_variable?? is a vector as an
        alternative to specifying a vector-valued expression in ??value??. ??value_x?? and
        ??value_y?? are also required if ??value_z?? is used.
            side_one_variable : str
                String specifying the name of the variable associated with side1
        of the interface. Must be combined with ??side_two_variable??. Used only
        when creating variable-based data transfers. Consider using
        ??source_variable??/??target_variable?? parameters instead.
            side_two_variable : str
                String specifying the name of the variable associated with side2
        of the interface. Must be combined with ??side_two_variable??. Used only
        when creating variable-based data transfers. Consider using
        ??source_variable??/??target_variable?? parameters instead.

        """

        syc_name = "AddDataTransfer"
        argument_names = [
            "interface",
            "target_side",
            "source_variable",
            "target_variable",
            "value",
            "value_x",
            "value_y",
            "value_z",
            "side_one_variable",
            "side_two_variable",
        ]
        essential_arguments = ["interface", "target_side"]

        class interface(String):
            """
            String indicating the name of the interface on which the data transfer
            is to be created.
            """

            syc_name = "Interface"

        class target_side(String):
            """
            String indicating the side of the interface to receive the data
            transfer variable. Possible values are 'One' or 'Two'.
            """

            syc_name = "TargetSide"

        class source_variable(String):
            """
            String specifying the name of the variable on the source side of
            the data transfer. Used when creating a variable-based data transfer.
            Must be combined with ??target_variable??.
            """

            syc_name = "SourceVariable"

        class target_variable(String):
            """
            String specifying the name of the variable on the target side of
            the data transfer. Must be combined with either ??source_variable?? (when
            creating a variable-based data transfer) or with ??value??{X|Y|Z}
            (when creating an expression-based data transfer).
            """

            syc_name = "TargetVariable"

        class value(String):
            """
            String specifying the expression to use on the source side of the data
            transfer. Used when creating an expression-based data transfer. If the
            ??target_variable?? is a vector, a vector-valued expression must be provided.
            Alternatively, ??value_x??, ??value_y??, ??value_z?? may be used to specify the
            individual components of the vector expression.
            """

            syc_name = "Value"

        class value_x(String):
            """
            String specifying the X component of the expression to use on the
            source side of the data transfer. This may optionally be used when creating
            an expression-based data transfer if the ??target_variable?? is a vector as an
            alternative to specifying a vector-valued expression in ??value??. ??value_y?? and
            ??value_z?? are also required if ??value_x?? is used.
            """

            syc_name = "ValueX"

        class value_y(String):
            """
            String specifying the Y component of the expression to use on the
            source side of the data transfer. This may optionally be used when creating
            an expression-based data transfer if the ??target_variable?? is a vector as an
            alternative to specifying a vector-valued expression in ??value??. ??value_x?? and
            ??value_z?? are also required if ??value_y?? is used.
            """

            syc_name = "ValueY"

        class value_z(String):
            """
            String specifying the Z component of the expression to use on the
            source side of the data transfer. This may optionally be used when creating
            an expression-based data transfer if the ??target_variable?? is a vector as an
            alternative to specifying a vector-valued expression in ??value??. ??value_x?? and
            ??value_y?? are also required if ??value_z?? is used.
            """

            syc_name = "ValueZ"

        class side_one_variable(String):
            """
            String specifying the name of the variable associated with side1
            of the interface. Must be combined with ??side_two_variable??. Used only
            when creating variable-based data transfers. Consider using
            ??source_variable??/??target_variable?? parameters instead.
            """

            syc_name = "SideOneVariable"

        class side_two_variable(String):
            """
            String specifying the name of the variable associated with side2
            of the interface. Must be combined with ??side_two_variable??. Used only
            when creating variable-based data transfers. Consider using
            ??source_variable??/??target_variable?? parameters instead.
            """

            syc_name = "SideTwoVariable"

    class add_data_transfer_by_display_names(Command):
        """
        Adds data transfer based on arguments that specify the interface, target
        side, and variables to be associated with each side of the interface.
        The command requires that you specify variables using their display names,
        as described below in Essential Keyword Arguments. Either a variable-based
        or expression-based data transfer may be created with this command based on
        the Optional Keyword Arguments. If a variable-based data transfer argument
        is given, then no expression-based data transfer arguments can be used. If
        an expression-based data transfer argument is given, then no variable-based
        data transfer arguments can be used.

        Cannot be run after participants have been started.

        Returns the name of the Data Transfer created.

        Parameters
        ----------
            interface : str
                String indicating the display name of the interface on which the
        data transfer is to be created.
            target_side : str
                String indicating the side of the interface to receive the data
        transfer variable. Possible values are 'One' or 'Two'.
            source_variable : str
                String specifying the display name of the variable on the source side of
        the data transfer. Used when creating a variable-based data transfer.
        Must be combined with ??target_variable??.
            target_variable : str
                String specifying the display name of the variable on the target side of
        the data transfer. Must be combined with either ??source_variable?? (when
        creating a variable-based data transfer) or with ??value??{X|Y|Z}
        (when creating an expression-based data transfer).
            value : str
                String specifying the expression to use on the source side of the data
        transfer. Used when creating an expression-based data transfer if the
        ??target_variable?? is a scalar. (If the ??target_variable?? is a vector,
        ??value_x??, ??value_y??, ??value_z?? must be used instead.)
            value_x : str
                String specifying the X component of the expression to use on the
        source side of the data transfer. Used when crating an expression-based
        data transfer if the ??target_variable?? is a vector. (If the ??target_variable??
        is scalar, ??value?? must be used instead.) ??value_y?? and ??value_z?? are also
        required if ??value_x?? is used.
            value_y : str
                String specifying the Y component of the expression to use on the
        source side of the data transfer. Used when crating an expression-based
        data transfer if the ??target_variable?? is a vector. (If the ??target_variable??
        is scalar, ??value?? must be used instead.) ??value_x?? and ??value_z?? are also
        required if ??value_y?? is used.
            value_z : str
                String specifying the Z component of the expression to use on the
        source side of the data transfer. Used when crating an expression-based
        data transfer if the ??target_variable?? is a vector. (If the ??target_variable??
        is scalar, ??value?? must be used instead.) ??value_x?? and ??value_y?? are also
        required if ??value_z?? is used.
            side_one_variable : str
                String specifying the display name of the variable associated with side1
        of the interface. Must be combined with ??side_two_variable??. Used only
        when creating variable-based data transfers. Consider using
        ??source_variable??/??target_variable?? parameters instead.
            side_two_variable : str
                String specifying the display name of the variable associated with side2
        of the interface. Must be combined with ??side_two_variable??. Used only
        when creating variable-based data transfers. Consider using
        ??source_variable??/??target_variable?? parameters instead.

        """

        syc_name = "AddDataTransferByDisplayNames"
        argument_names = [
            "interface",
            "target_side",
            "source_variable",
            "target_variable",
            "value",
            "value_x",
            "value_y",
            "value_z",
            "side_one_variable",
            "side_two_variable",
        ]
        essential_arguments = ["interface", "target_side"]

        class interface(String):
            """
            String indicating the display name of the interface on which the
            data transfer is to be created.
            """

            syc_name = "Interface"

        class target_side(String):
            """
            String indicating the side of the interface to receive the data
            transfer variable. Possible values are 'One' or 'Two'.
            """

            syc_name = "TargetSide"

        class source_variable(String):
            """
            String specifying the display name of the variable on the source side of
            the data transfer. Used when creating a variable-based data transfer.
            Must be combined with ??target_variable??.
            """

            syc_name = "SourceVariable"

        class target_variable(String):
            """
            String specifying the display name of the variable on the target side of
            the data transfer. Must be combined with either ??source_variable?? (when
            creating a variable-based data transfer) or with ??value??{X|Y|Z}
            (when creating an expression-based data transfer).
            """

            syc_name = "TargetVariable"

        class value(String):
            """
            String specifying the expression to use on the source side of the data
            transfer. Used when creating an expression-based data transfer if the
            ??target_variable?? is a scalar. (If the ??target_variable?? is a vector,
            ??value_x??, ??value_y??, ??value_z?? must be used instead.)
            """

            syc_name = "Value"

        class value_x(String):
            """
            String specifying the X component of the expression to use on the
            source side of the data transfer. Used when crating an expression-based
            data transfer if the ??target_variable?? is a vector. (If the ??target_variable??
            is scalar, ??value?? must be used instead.) ??value_y?? and ??value_z?? are also
            required if ??value_x?? is used.
            """

            syc_name = "ValueX"

        class value_y(String):
            """
            String specifying the Y component of the expression to use on the
            source side of the data transfer. Used when crating an expression-based
            data transfer if the ??target_variable?? is a vector. (If the ??target_variable??
            is scalar, ??value?? must be used instead.) ??value_x?? and ??value_z?? are also
            required if ??value_y?? is used.
            """

            syc_name = "ValueY"

        class value_z(String):
            """
            String specifying the Z component of the expression to use on the
            source side of the data transfer. Used when crating an expression-based
            data transfer if the ??target_variable?? is a vector. (If the ??target_variable??
            is scalar, ??value?? must be used instead.) ??value_x?? and ??value_y?? are also
            required if ??value_z?? is used.
            """

            syc_name = "ValueZ"

        class side_one_variable(String):
            """
            String specifying the display name of the variable associated with side1
            of the interface. Must be combined with ??side_two_variable??. Used only
            when creating variable-based data transfers. Consider using
            ??source_variable??/??target_variable?? parameters instead.
            """

            syc_name = "SideOneVariable"

        class side_two_variable(String):
            """
            String specifying the display name of the variable associated with side2
            of the interface. Must be combined with ??side_two_variable??. Used only
            when creating variable-based data transfers. Consider using
            ??source_variable??/??target_variable?? parameters instead.
            """

            syc_name = "SideTwoVariable"

    class get_region_names_for_participant(Command):
        """
        Gets all of the specified participant's regions.

        Returns a dictionary with the regions as keys and the corresponding
        display names as values.

        Parameters
        ----------
            participant_name : str
                String indicating the participant for which regions are returned.

        """

        syc_name = "GetRegionNamesForParticipant"
        argument_names = ["participant_name"]
        essential_arguments = ["participant_name"]

        class participant_name(String):
            """
            String indicating the participant for which regions are returned.
            """

            syc_name = "ParticipantName"

    class add_reference_frame(Command):
        """
        Add a reference frame to the datamodel

        The function will add a blank reference frame to the datamodel. Any
        transformations must be added separately.

        Reference frame name will be "Frame-#" where # is the first positive
        integer which yields a unique frame name.

        Returns the name of the reference frame.

        Parameters
        ----------
            parent_reference_frame : str
                Name of a reference frame that the added frame should use as the
        parent. If the argument is not provided, the default parent reference
        frame "GlobalReferenceFrame" will be added.

        """

        syc_name = "AddReferenceFrame"
        argument_names = ["parent_reference_frame"]
        essential_arguments = []

        class parent_reference_frame(String):
            """
            Name of a reference frame that the added frame should use as the
            parent. If the argument is not provided, the default parent reference
            frame "GlobalReferenceFrame" will be added.
            """

            syc_name = "ParentReferenceFrame"

    class add_transformation(Command):
        """
        Add a transformation to a reference frame defined in the datamodel

        Given the reference frame to add to the transform to, the type of transform
        to be added, and any required information for the transformation, add the
        transformation to the referenceFrame. Not all parameters are required for
        every transformation.

        The name of the transformation will be based on the type of transformation.
        The name will be of the form "<??transformation_type??>-#" where # is the first
        positive integer which yields a unique frame name.

        The transformation will also be added to the end of the ??transformation_order??
        list for the reference frame.

        Returns the name of the transformation.

        Parameters
        ----------
            reference_frame : str
                Name of the reference frame to which the transformation will be added.
            transformation_type : str
                ??type?? of transformation to be added. Available options are Rotation or
        Translation

        Required Parameters for ??transformation?? Types:
            Rotation: ??angle??, ??axis??, ??vector?? (if ??axis?? is "UserDefined")
            Translation: ??vector??
            angle : real
                ??angle?? to rotate a reference frame. Used with Rotation
        ??transformation_type??. Default unit is Radians.
            axis : str
                ??axis?? about which a rotation is applied. Used with
        Rotation ??transformation_type??. Available options are: "XAxis", "YAxis",
        "ZAxis", and "UserDefined".
            vector : typing.Tuple[real, real, real]
                A vector for use with Translation ??transformation_type?? or Rotation
        ??transformation_type?? if the ??axis?? is "UserDefined".

        """

        syc_name = "AddTransformation"
        argument_names = [
            "reference_frame",
            "transformation_type",
            "angle",
            "axis",
            "vector",
        ]
        essential_arguments = ["reference_frame", "transformation_type"]

        class reference_frame(String):
            """
            Name of the reference frame to which the transformation will be added.
            """

            syc_name = "ReferenceFrame"

        class transformation_type(String):
            """
            ??type?? of transformation to be added. Available options are Rotation or
            Translation

            Required Parameters for ??transformation?? Types:
                Rotation: ??angle??, ??axis??, ??vector?? (if ??axis?? is "UserDefined")
                Translation: ??vector??
            """

            syc_name = "TransformationType"

        class angle(Real):
            """
            ??angle?? to rotate a reference frame. Used with Rotation
            ??transformation_type??. Default unit is Radians.
            """

            syc_name = "Angle"

        class axis(String):
            """
            ??axis?? about which a rotation is applied. Used with
            Rotation ??transformation_type??. Available options are: "XAxis", "YAxis",
            "ZAxis", and "UserDefined".
            """

            syc_name = "Axis"

        class vector(RealVector):
            """
            A vector for use with Translation ??transformation_type?? or Rotation
            ??transformation_type?? if the ??axis?? is "UserDefined".
            """

            syc_name = "Vector"

    class delete_transformation(Command):
        """
        Delete a transformation from a reference frame

        In addition to deleting the transformation object, it will also remove the
        transformation from ??transformation_order?? (if it exists in that list).

        Parameters
        ----------
            reference_frame : str
                Name of the reference frame from which the transformation will be
        deleted.
            transformation_name : str
                Name of the transformation which will be deleted.

        """

        syc_name = "DeleteTransformation"
        argument_names = ["reference_frame", "transformation_name"]
        essential_arguments = ["reference_frame", "transformation_name"]

        class reference_frame(String):
            """
            Name of the reference frame from which the transformation will be
            deleted.
            """

            syc_name = "ReferenceFrame"

        class transformation_name(String):
            """
            Name of the transformation which will be deleted.
            """

            syc_name = "TransformationName"

    class add_participant(Command):
        """
        Adds a coupling participant to the data model.

        When executed, this command adds the new participant to the analysis
        without removing any interfaces or data transfers created previously.

        Cannot be called after participants have been started.

        Returns the name of the participant.

        There are two options to add the participant - via a file, or via a
        participant executable.

        ??option?? 1: Using an input file

        Given an input file containing participant coupling information, reads the
        specified file, pushes the participant's information to the data model.

        ??option?? 2: Using a participant executable

        Given the path to the executable for this participant (and optionally,
        additional arguments and/or working directory), start the participant
        executable, connect to the participant using the socket connection,
        and get the participant's information and add it to the data model.

        Parameters
        ----------
            participant_type : str
                Participant type. Currently supported types are DEFAULT, CFX, FLUENT,
        MAPDL, AEDT, FMU, FORTE, DEFAULT-SRV, MECH-SRV, CFD-SRV. If
        unspecified, ??add_participant?? will attempt to deduce the type from
        ??input_file??.
            input_file : str
                Name of the input file for the participant to be added.
        Currently supported formats are SCP files, Forte input (FTSIM) files,
        and FMU (.fmu) files (Beta).
            executable : str
                Path to the executable file for the participant to be added.
            additional_arguments : str
                Any additional arguments to be passed to the participant's executable.
            working_directory : str
                Path to the working directory for this participant.

        """

        syc_name = "AddParticipant"
        argument_names = [
            "participant_type",
            "input_file",
            "executable",
            "additional_arguments",
            "working_directory",
        ]
        essential_arguments = []

        class participant_type(String):
            """
            Participant type. Currently supported types are DEFAULT, CFX, FLUENT,
            MAPDL, AEDT, FMU, FORTE, DEFAULT-SRV, MECH-SRV, CFD-SRV. If
            unspecified, ??add_participant?? will attempt to deduce the type from
            ??input_file??.
            """

            syc_name = "ParticipantType"

        class input_file(String):
            """
            Name of the input file for the participant to be added.
            Currently supported formats are SCP files, Forte input (FTSIM) files,
            and FMU (.fmu) files (Beta).
            """

            syc_name = "InputFile"

        class executable(String):
            """
            Path to the executable file for the participant to be added.
            """

            syc_name = "Executable"

        class additional_arguments(String):
            """
            Any additional arguments to be passed to the participant's executable.
            """

            syc_name = "AdditionalArguments"

        class working_directory(String):
            """
            Path to the working directory for this participant.
            """

            syc_name = "WorkingDirectory"

    class import_system_coupling_input_file(Command):
        """
        Reads the specified System Coupling SCI file and pushes its information
        into the data model. The SCI file is the required System Coupling input
        format for the initial run of a coupled analysis set up in Workbench.

        After the initial run based on an imported SCI file, a reissue
        of the ??import_system_coupling_input_file?? command is unnecessary and is
        not recommended unless the setup has changed.

        Cannot be run after participants have been started.

        Parameters
        ----------
            file_path : str
                Path and file name for the SCI file to be read.

        """

        syc_name = "ImportSystemCouplingInputFile"
        argument_names = ["file_path"]
        essential_arguments = ["file_path"]

        class file_path(String):
            """
            Path and file name for the SCI file to be read.
            """

            syc_name = "FilePath"

    class get_expression_variables(PathCommand):
        """
        Given a path to an object return a list of variables which can be used in
        an expression on the object. A parameter name may be provided, in which
        case the list of variables returned is that which is available for use in
        an expression assigned to that parameter.

        The variable is a tuple of strings: the variable name, the unit string of
        the variable (in the defined unit system), and the tensor type of the
        variable (e.g. scalar or vector).

        If an expression can not be used on the object or if there are no valid
        variables which can be used in the expression, the no output will be
        returned.

        For the purposes of the command, "valid" means that the variable may be
        used in the expression. Note however that "valid" does not necessarily mean
        that a variable can be used in the expression. Other validation rules may
        preclude the use of the variable. See the user documentation for more
        details.

        The list of variables will be ordered with the most likely variables first.
        That is, those sharing the same quantity type and/or dimensionality as the
        target of the expression.

        Parameters
        ----------
            parameter_name : str
                String indicating the name of the parameter to get expression
        variables for.

        """

        syc_name = "GetExpressionVariables"
        argument_names = ["parameter_name"]
        essential_arguments = ["object_path"]

        class parameter_name(String):
            """
            String indicating the name of the parameter to get expression
            variables for.
            """

            syc_name = "ParameterName"

    class add_default_transformation(Command):
        """
        Add a default transformation to a reference frame defined in the datamodel

        Given the reference frame to add to the transform to and the type of
        transform to be added, a minimally defined transformation will be
        constructed. Any information required for the transformation (e.g. angle
        and axis for a rotation) will have their default values.

        The name of the transformation will be based on the type of transformation.
        The name will be of the form "<??transformation_type??>-#" where # is the first
        positive integer which yields a unique frame name.

        The transformation will also be added to the end of the ??transformation_order??
        list for the reference frame.

        Returns the name of the transformation.

        Parameters
        ----------
            reference_frame : str
                Name of the reference frame to which the transformation will be added.
            transformation_type : str
                ??type?? of transformation to be added. Available options are Rotation,
        Translation, or Reflection (alpha only).

        """

        syc_name = "AddDefaultTransformation"
        argument_names = ["reference_frame", "transformation_type"]
        essential_arguments = ["reference_frame", "transformation_type"]

        class reference_frame(String):
            """
            Name of the reference frame to which the transformation will be added.
            """

            syc_name = "ReferenceFrame"

        class transformation_type(String):
            """
            ??type?? of transformation to be added. Available options are Rotation,
            Translation, or Reflection (alpha only).
            """

            syc_name = "TransformationType"

    class add_instancing(Command):
        """
        Add a instancing object to the datamodel

        Without optional arguments, constructs a default instancing object with the
        next available instancing name. The name will be of the form "??instancing??-#"
        where "#" is the first unused integer value starting from 1.

        Returns the name of the instancing object.

        Parameters
        ----------
            reference_frame : str
                Name of the reference frame used to define the orientation of the
        instancing.
            instances_in_full_circle : int
                The number of instances that would exist if the original mesh was
        replicated about 360 degrees. This value includes the original mesh
        instance. If the mapping should not use all instances for mapping,
        use the optional argument ??instances_for_mapping??.
            instances_for_mapping : int
                The number of instances that will be included when instancing is
        applied. Not required unless the number of instances to be used for
        mapping does not match the number of instances in a full circle. If
        this argument is not provided, then the value will be automatically set
        to ??instances_in_full_circle??. This value includes the original mesh
        instance.

        """

        syc_name = "AddInstancing"
        argument_names = [
            "reference_frame",
            "instances_in_full_circle",
            "instances_for_mapping",
        ]
        essential_arguments = []

        class reference_frame(String):
            """
            Name of the reference frame used to define the orientation of the
            instancing.
            """

            syc_name = "ReferenceFrame"

        class instances_in_full_circle(Integer):
            """
            The number of instances that would exist if the original mesh was
            replicated about 360 degrees. This value includes the original mesh
            instance. If the mapping should not use all instances for mapping,
            use the optional argument ??instances_for_mapping??.
            """

            syc_name = "InstancesInFullCircle"

        class instances_for_mapping(Integer):
            """
            The number of instances that will be included when instancing is
            applied. Not required unless the number of instances to be used for
            mapping does not match the number of instances in a full circle. If
            this argument is not provided, then the value will be automatically set
            to ??instances_in_full_circle??. This value includes the original mesh
            instance.
            """

            syc_name = "InstancesForMapping"

    class get_errors(Command):
        """
        If errors exist, returns them as a list of dictionaries containing error
        details; otherwise, returns an empty list. See also: ??get_errors_xml??().
        """

        syc_name = "GetErrors"

    class add_named_expression(Command):
        """
        Creates a named expression object in the data model.
        If there is already an object in the data model whose '??expression_name??'
        matches the provided ??expression_name??, its '??expression_string??' will be
        overwritten with the provided ??expression_string??

        Parameters
        ----------
            expression_name : str
                The name by which this expression should be referenced when used in
        another expression.
            expression_string : str
                String containing the definition of the expression.

        """

        syc_name = "AddNamedExpression"
        argument_names = ["expression_name", "expression_string"]
        essential_arguments = ["expression_name", "expression_string"]

        class expression_name(String):
            """
            The name by which this expression should be referenced when used in
            another expression.
            """

            syc_name = "ExpressionName"

        class expression_string(String):
            """
            String containing the definition of the expression.
            """

            syc_name = "ExpressionString"

    class add_expression_function(Command):
        """
        Creates an expression function object in the data model that makes
        available an external Python function for use in expressions.

        The parameters specified should correspond to a module and function
        that exists and can successfully be loaded when the application
        starts. Otherwise, the data model object will be created but there
        will be validation errors and the function will not be available for
        use.

        Parameters
        ----------
            module : str
                The name of the Python module (in the 'Modules' sub-directory of
        the working directory) from which the function is to be obtained.
            function : str
                The name of the function in the module. If no ??function_name?? is
        specified, this will also be the name by which the function should
        be referenced when used in an expression.
            function_name : str
                Optionally specify a different name from ??function?? which should be
        the name used to reference the function in an expression.

        """

        syc_name = "AddExpressionFunction"
        argument_names = ["module", "function", "function_name"]
        essential_arguments = ["module", "function"]

        class module(String):
            """
            The name of the Python module (in the 'Modules' sub-directory of
            the working directory) from which the function is to be obtained.
            """

            syc_name = "Module"

        class function(String):
            """
            The name of the function in the module. If no ??function_name?? is
            specified, this will also be the name by which the function should
            be referenced when used in an expression.
            """

            syc_name = "Function"

        class function_name(String):
            """
            Optionally specify a different name from ??function?? which should be
            the name used to reference the function in an expression.
            """

            syc_name = "FunctionName"

    class reload_expression_function_modules(Command):
        """
        This may be called to force a reload of expression function modules
        if they have changed since they were last loaded.
        """

        syc_name = "ReloadExpressionFunctionModules"
