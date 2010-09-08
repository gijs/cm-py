from Soap import *
from settings import CAMPAIGN_MONITOR_NAMESPACE, CAMPAIGN_MONITOR_URL

class CampaignMonitor(SoapObject):
    
    def __init__(self, api_key=None, **kwargs):
        self.extra_keys['ApiKey'] = api_key or getattr(settings, 'CAMPAIGN_MONITOR_KEY')
        SoapObject.__init__(self, CAMPAIGN_MONITOR_NAMESPACE, CAMPAIGN_MONITOR_URL, self.parse, True, **kwargs)
    
    def parse(self, method, soap_resp):
        doc = minidom.parseString(soap_resp)
        if doc.hasChildNodes():
            result_nodes = doc.getElementsByTagName(method+"Result")
            if len(result_nodes) == 1:
                node = result_nodes[0]
                rtype = node._attrs.get('xsi:type')
                if rtype: rtype = rtype.value
                else: rtype='boop'
                if not node.firstChild.hasChildNodes(): return node.firstChild.nodeValue
                elif rtype.startswith('Array'):
                    arr = []
                    for node_list in node.childNodes:
                        node_info = {}
                        for i in node_list.childNodes:
<<<<<<< HEAD
                            if i.firstChild:
                                node_info[i.nodeName] = i.firstChild.nodeValue
=======
                            node_info[i.nodeName] = i.firstChild.nodeValue
>>>>>>> d7a0cabc74141b1b6ff5056f4cbc3d2c5e9eddff
                        arr.append(node_info)
                    
                    return arr
                elif rtype.startswith('Client'):
                    node_info = {}
                    for i in node.childNodes:
                        node_info[i.nodeName] = {}
                        for ii in i.childNodes:
                            if ii.firstChild: node_info[i.nodeName][ii.nodeName] = ii.firstChild.nodeValue
                            else: node_info[i.nodeName][ii.nodeName] = ii.nodeValue
                    return node_info
                else:
                    node_info = {}
                    for i in node.childNodes:
                        node_info[i.nodeName] = i.firstChild.nodeValue
                    
                    return node_info
        return None
        

class Client(CampaignMonitor): pass

class List(CampaignMonitor): pass
        
class Subscriber(CampaignMonitor): pass
        
class Subscribers(CampaignMonitor): pass

class Template(CampaignMonitor): pass

class Campaign(CampaignMonitor): pass
    
class User(CampaignMonitor): pass