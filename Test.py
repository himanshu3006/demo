from create_gluster import creategluster, delete_gluster
import logging
from create_gluster import gluster_status, fio_start, fio_install
import unittest
import testlink
import os
import xml.etree.ElementTree as ET
from testLinkLibrary import *
import PyUnitReport


class Testt(unittest.TestCase):

    def setUp(self):
        print "before setup"
        #self.install_gluster = creategluster()
        # self.assertAlmostEquals()=creategluster()
        # fio_install()
        print "After setup"

    #def test_triggering_io_jobs(self):
    def test_A_gluster_status(self):
        print "before trigger"
        gluster_status()
	#result= self.assertEqual(3+3, 5)
	result='FAIL'
	if(result=='FAIL'):
        	'''
                	This function defines the sequence under which a
                	particular test case will go.
        	'''
        	# setting the result to be true initially
        	result = "PASS"
        	self.testLinkTCName = ['Create Gluster']
        	tls = getTestLinkObject(result_dict['testLinkURL'], result_dict['testLinkDEVKEY'])

        	addBuildToTestPlan(tls, result_dict['testLinkTestProjectName'], result_dict['testLinkTestPlanName'],  result_dict['testLinkBuildName'], "fROM AUT")
        	for name in self.testLinkTCName:
        		# if user wants to upload result in TestLink
            	   if result_dict['uploadResultInTestLink'] == 'True' and name != '':
                      try:
                	# establish connection with TestLink


                    	# testCaseStatus is 'p' for PASS and 'f' for FAIL
                          testCaseStatus = ''
                    	  if result == "PASS":
                             testCaseStatus = 'p'
                    	  else:
                             testCaseStatus = 'f'

                          updateResultInTestLink(tls, result_dict['testLinkTestProjectName'], result_dict['testLinkTestPlanName'], result_dict[
                                       'testLinkBuildName'],name, testCaseStatus, result_dict['testLinkPlatform'])
                      except Exception as e:
                         print('Error "%s" while updating result in TestLink' % e)

        print "After io trigger"

    def test_B_start_fio(self):
        print "Before start FIO"
	fio_start()
	result='FAIL'
        if(result=='FAIL'):
                '''
                        This function defines the sequence under which a
                        particular test case will go.
                '''
                # setting the result to be true initially
                result = "FAIL"
                self.testLinkTCName = ['Gluster Status']
                tls = getTestLinkObject(result_dict['testLinkURL'], result_dict['testLinkDEVKEY'])

                addBuildToTestPlan(tls, result_dict['testLinkTestProjectName'], result_dict['testLinkTestPlanName'],  result_dict['testLinkBuildName'], "fROM AUT")
                for name in self.testLinkTCName:
                        # if user wants to upload result in TestLink
                   if result_dict['uploadResultInTestLink'] == 'True' and name != '':
                      try:
                        # establish connection with TestLink


                        # testCaseStatus is 'p' for PASS and 'f' for FAIL
                          testCaseStatus = ''
                          if result == "PASS":
                             testCaseStatus = 'p'
                          else:
                             testCaseStatus = 'f'

                          updateResultInTestLink(tls, result_dict['testLinkTestProjectName'], result_dict['testLinkTestPlanName'], result_dict[
                                       'testLinkBuildName'],name, testCaseStatus, result_dict['testLinkPlatform'])
                      except Exception as e:
                         print('Error "%s" while updating result in TestLink' % e)


	print "After Completion FIO Jobs"

    def test_C_status_aft_comp(self):
	print "Before checking status"
	gluster_status()
	#self.assertEqual(3+3, 7)
	result='FAIL'
        if(result=='FAIL'):
                '''
                        This function defines the sequence under which a
                        particular test case will go.
                '''
                # setting the result to be true initially
                result = "PASS"
                self.testLinkTCName = ['FIO Start']
                tls = getTestLinkObject(result_dict['testLinkURL'], result_dict['testLinkDEVKEY'])

                addBuildToTestPlan(tls, result_dict['testLinkTestProjectName'], result_dict['testLinkTestPlanName'],  result_dict['testLinkBuildName'], "fROM AUT")
                for name in self.testLinkTCName:
                        # if user wants to upload result in TestLink
                   if result_dict['uploadResultInTestLink'] == 'True' and name != '':
                      try:
                        # establish connection with TestLink


                        # testCaseStatus is 'p' for PASS and 'f' for FAIL
                          testCaseStatus = ''
                          if result == "PASS":
                             testCaseStatus = 'p'
                          else:
                             testCaseStatus = 'f'

                          updateResultInTestLink(tls, result_dict['testLinkTestProjectName'], result_dict['testLinkTestPlanName'], result_dict[
                                       'testLinkBuildName'],name, testCaseStatus, result_dict['testLinkPlatform'])
                      except Exception as e:
                         print('Error "%s" while updating result in TestLink' % e)


	print "After checking status"

    def tearDown(self):
       print "before teardown"
      #delete_gluster()
       #self.assertEqual(3+3, 6)
       print "before teardown"


if __name__ == "__main__":
    #unittest.main()
    print "Starting Test"
    # Test()
    tree = ET.parse(os.path.dirname(os.path.abspath(__file__)) + os.sep + 'ConfigInput.xml')
    #root = tree.getroot()

    for node in tree.iter():
        if node.tag == "Parameters":
            result_dict=node.attrib
            print result_dict
    unittest.main(testRunner=PyUnitReport.HTMLTestRunner(output='Result'))
