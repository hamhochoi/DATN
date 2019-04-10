class SmartContext():
    """
    Smart Context Object
    :param      smart_context_id            (string)
    :param      smart_context_name          (string)
    :param      is_sub_smart_context_of     (list)
    :param      has_sub_smart_context       (list)
    :param      has_platform                (list)
    """

    def __init__(self, smart_context_id, smart_context_name, 
                is_sub_smart_context_of, has_sub_smart_context, has_platform):
        pass


class Platform():
    """
    Platform Object
    :param      platform_id         (string)
    :param      platform_name       (string)
    :param      has_source          (list)
    """

    def __init__(self, platform_id, platform_name,
                 has_source, belong_smartcontext):
        pass


class Source():
    """
    Source Object
    :param      source_global_id : unified id of sources            (string)
    :param      source_local_id  : source id in each platform       (string)
    :param      source_name                                         (string)
    :param      has_thing                                           (list)
    :param      has_metric                                          (list)
    :param      has_type                                            (string)
    """

    def __init__(self, source_global_id, source_local_id, 
                source_name, has_thing, has_metric,
                has_type, belong_platform):
        pass

    
class Thing():
    """
    Thing Object
    :param      thing_id        (string)
    :param      thing_name      (string)
    """

    def __init__(self, thing_id, thing_name,
                 thing_belong_source):
        pass


class Metric():
    """
    Metric Object
    :param      metric_global_id : unified id of metric on the cross platform       (string)
    :param      metric_local_id  : metric id in each platform                       (string)
    :param      metric_name                                                         (string)
    :param      metric_status                                                       (string)
    :param      can_set_state    : is metric can set state by api or not            (True/False - string)
    :param      has_unit         : unit of metric                                   (degree/percent/time - string)
    """

    def __init__(self, metric_global_id, metric_local_id, 
                 metric_name, metric_status, 
                 can_set_state, has_unit
                 metric_belong_source):
        pass


class DataPoint():
    """
    DataPoint Object
    :param      belong_metric    : which metric this data point is belonged to         (string)
    :param      has_time_collect : time when this data point is collected              (string)
    :param      has_value        : value of data point                                 (string/number)
    :param      has_data_type                                                          (string)
    """
    def __init__(self, belong_metric, has_time_collect, 
                has_value, has_data_type):
        pass