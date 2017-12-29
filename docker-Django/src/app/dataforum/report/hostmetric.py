from report.models import Host, Oracle

def host_metric_test():
    """
    List all Hosts
    """
    Host.objects.create()
