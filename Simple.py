from create_gluster import creategluster, delete_gluster
from create_gluster import gluster_status, fio_start, fio_install
import unittest
import testlink
import os
import xml.etree.ElementTree as ET
from testLinkLibrary import *
import argparse
from robot.api import ExecutionResult, SuiteVisitor

class PrintTestInfo(SuiteVisitor):
   def __init__(self,jenkins_build=''):
      self.build=jekins_build
      self.result='PASS'
 
class Test(unittest.TestCase):

    def setUp(self):
        print "before setup"
        #self.install_gluster = creategluster()
        # self.assertAlmostEquals()=creategluster()
        # fio_install()
        print "After setup"

    #def test_triggering_io_jobs(self):
    def test_C_gluster_status(self, build_id=''):
	self.build=jenkins_build
        self.result = {}

        print "before trigger"
        self.gluster_status()
	#result= self.assertEqual(3+3, 5)
#	result='FAIL'
	#result= self.assertEqual(3+3, 5)
 #       result='FAIL'
#class PrintTestInfo(SuiteVisitor):
  #  def __init__(self,jenkins_build=''):
   #     self.build=jenkins_build
  #      self.result = {}


        tree = ET.parse(os.path.dirname(os.path.abspath(__file__)) + os.sep + 'ConfigInput.xml')
        for node in tree.iter():
            if node.tag == "Parameters":
                self.result_dict = node.attrib
        self.tls = getTestLinkObject(
            self.result_dict['testLinkURL'], self.result_dict['testLinkDEVKEY'])
        addBuildToTestPlan(self.tls, self.result_dict['testLinkTestProjectName'], self.result_dict['testLinkTestPlanName'],
                           self.build, "fROM AUT")

    def visit_test(self, Test):
        if test.status == "PASS":
            testCaseStatus = 'p'
        else:
            testCaseStatus = 'f'

        updateResultInTestLink(self.tls, self.result_dict['testLinkTestProjectName'], self.result_dict['testLinkTestPlanName'],
                               self.build, test.name.strip(":"),testCaseStatus, self.result_dict['testLinkPlatform'])


if __name__ == "__main__":
    #unittest.main()
    print "Starting Test"
    #Test()
    
    parser = argparse.ArgumentParser(description="Gluster Framework")
    parser.add_argument("-b", action="store", default="False", dest="build_id")
    command_args = parser.parse_args()

    tree = ET.parse(os.path.dirname(os.path.abspath(__file__)) + os.sep + 'ConfigInput.xml')
    #root = tree.getroot()

#   if command_args.build_id:
#      print "running"
#      Test.test_B_gluster_status('True',command_args.build_id)
#   else:
#      Test.test_B_gluster_status()	

    for node in tree.iter():
        if node.tag == "Parameters":
            result_dict=node.attrib
            print result_dict

    unittest.main()
