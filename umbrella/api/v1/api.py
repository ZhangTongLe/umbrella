# Copyright 2013 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
"""


from oslo_config import cfg
from oslo_log import log as logging
from umbrella.common import wsgi
from umbrella import i18n
from umbrella.db.sqlalchemy import api as db_api
from umbrella.db.sqlalchemy import models
import time
import json
import collections

LOG = logging.getLogger(__name__)
_ = i18n._
_LE = i18n._LE
_LI = i18n._LI
_LW = i18n._LW

CONF = cfg.CONF


class Controller():
    """
    WSGI controller for api resource in Umbrella v1 API

    The resource API is a RESTful web service for image data. The API
    is as follows::

        GET /api/{net,cpu,disk,mem}/instance-uuid?from=time1&&to=time2
        -- Returns a set of
        resource data
    """

    def __init__(self):
        #self.notifier = notifier.Notifier()
        #registry.configure_registry_client()
        #self.policy = policy.Enforcer()
        #if property_utils.is_property_protection_enabled():
        #    self.prop_enforcer = property_utils.PropertyRules(self.policy)
        #else:
        #    self.prop_enforcer = None
        pass

    def index(self, req):
        #db_api.create_one_net()
        #aa = db_api.get_one_net()
        params = {}

        params.update(req.GET)
        return params
        return {"a": "b", "c": "d"}

    def show(self, req, id):
        #db_api.create_one_net()
        #aa = db_api.get_one_net()
        return {"show":"show"}

    def time_format(self,timeValue):
        timeStamp = int(time.mktime(time.strptime(timeValue,"%Y-%m-%dT%H-%M-%SZ")))
        #print "time ========",timeStamp
        timeArray = time.localtime(timeStamp)
        timeStr=time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        #print "timeStr ======",timeStr
        return timeStr

    def get_net_sample(self, req, instance_uuid):
        #import ipdb; ipdb.set_trace() ### XXX BREAKPOINT
        params = {}
        params.update(req.GET)
        
        start = self.time_format(params['start'])
        end = self.time_format(params['end'])
        session = db_api.get_session()
        query = session.query(models.Net)
        print "params = %s,%s" % (params['start'],params['end'])
        queryList = session.query(models.Net).filter(models.Net.instance_uuid == "%s" % instance_uuid,models.Net.created_at >= "%s" % start,models.Net.created_at <= "%s" % end).group_by(models.Net.id).all()
        print "*"*40,type(queryList)
        print queryList
        
        queryJson = []
        for item in queryList:
            queryDict = collections.OrderedDict()
            #queryDict = {}
            queryDict['id'] = item.id
            queryDict['instance_uuid'] = item.instance_uuid
            queryDict['tenant_id'] = item.tenant_id 
            queryDict['rx_packets_rate'] = item.rx_packets_rate
            queryDict['rx_bytes_rate'] = item.rx_bytes_rate
            queryDict['tx_packets_rate'] = item.tx_packets_rate
            queryDict['tx_bytes_rate'] = item.tx_bytes_rate
            queryDict['created_at'] = item.created_at
            queryDict['updated_at'] = item.updated_at
            queryJson.append(queryDict)
        return queryJson
        #return queryList       

    def get_disk_sample(self, req, instance_uuid):
        #import ipdb; ipdb.set_trace() ### XXX BREAKPOINT
        params = {}
        params.update(req.GET)

        start = self.time_format(params['start'])
        end = self.time_format(params['end'])
        session = db_api.get_session()
        query = session.query(models.Disk)
        print "params = %s,%s" % (params['start'],params['end'])
        queryList = session.query(models.Disk).filter(models.Disk.instance_uuid == "%s" % instance_uuid,models.Disk.created_at >= "%s" % start,models.Disk.created_at <= "%s" % end).group_by(models.Disk.id).all()
        print "*"*40,type(queryList)
        print queryList
        
        queryJson = []
        for item in queryList:
            queryDict = collections.OrderedDict()
            #queryDict = {}
            queryDict['id'] = item.id
            queryDict['instance_uuid'] = item.instance_uuid
            queryDict['tenant_id'] = item.tenant_id 
            queryDict['rd_req_rate'] = item.rd_req_rate
            queryDict['rd_bytes_rate'] = item.rd_bytes_rate
            queryDict['wr_req_rate'] = item.wr_req_rate
            queryDict['wr_bytes_rate'] = item.wr_bytes_rate
            queryDict['created_at'] = item.created_at
            queryDict['updated_at'] = item.updated_at
            queryJson.append(queryDict)
        return queryJson
            #return queryList

    def get_cpu_sample(self, req, instance_uuid):
        params = {}
        params.update(req.GET)


        start = self.time_format(params['start'])
        end = self.time_format(params['end'])
        session = db_api.get_session()
        query = session.query(models.Cpu)
        print "params = %s,%s" % (params['start'],params['end'])
        queryList = session.query(models.Cpu).filter(models.Cpu.instance_uuid == "%s" % instance_uuid,models.Cpu.created_at >= "%s" % start,models.Cpu.created_at <= "%s" % end).group_by(models.Cpu.id).all()
        print "*"*40,type(queryList)
        print queryList
        
        queryJson = []
        for item in queryList:
            queryDict = collections.OrderedDict()
            #queryDict = {}
            queryDict['id'] = item.id
            queryDict['instance_uuid'] = item.instance_uuid
            queryDict['tenant_id'] = item.tenant_id 
            queryDict['cpu_load'] = item.cpu_load
            queryDict['created_at'] = item.created_at
            queryDict['updated_at'] = item.updated_at
            queryJson.append(queryDict)
        return queryJson
        #return queryList

    def get_mem_sample(self, req, instance_uuid):
        params = {}
        params.update(req.GET)

        start = self.time_format(params['start'])
        end = self.time_format(params['end'])
        session = db_api.get_session()
        query = session.query(models.Mem)
        print "params = %s,%s" % (params['start'],params['end'])
        queryList = session.query(models.Mem).filter(models.Mem.instance_uuid == "%s" % instance_uuid,models.Mem.created_at >= "%s" % start,models.Mem.created_at <= "%s" % end).group_by(models.Mem.id).all()
        print "*"*40,type(queryList)
        print queryList
        
        queryJson = []
        for item in queryList:
            queryDict = collections.OrderedDict()
            #queryDict = {}
            queryDict['id'] = item.id
            queryDict['instance_uuid'] = item.instance_uuid
            queryDict['tenant_id'] = item.tenant_id 
            queryDict['mem_used'] = item.mem_used
            queryDict['created_at'] = item.created_at
            queryDict['updated_at'] = item.updated_at
            queryJson.append(queryDict)
        return queryJson
        #return queryList

def create_resource():
    """Images resource factory method"""
    #deserializer = ImageDeserializer()
    #serializer = ImageSerializer()
    return wsgi.Resource(Controller())
