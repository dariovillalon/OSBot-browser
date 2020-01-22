from unittest import TestCase

from gw_bot.helpers.Test_Helper import Test_Helper
from osbot_browser.browser.Browser_Lamdba_Helper import Browser_Lamdba_Helper
from osbot_browser.view_helpers.VivaGraph_Js_Views import VivaGraph_Js_Views


class Test_VivaGraph_Js_Views(Test_Helper):

    def setUp(self):
        super().setUp()
        self.graph_name = 'graph_XKW'
        self.png_data   = None

    def tearDown(self):
        if self.png_data:
            Browser_Lamdba_Helper(headless=False).save_png_data(self.png_data)

    def test_default(self):
        graph_name = 'graph_J2O'
        self.png_data = VivaGraph_Js_Views.default(params=[graph_name])
        #self.png_data = False

        #return
    def test_default__with_non_issue_nodes(self):
        graph_name = 'graph_THV'                    # create by an group_by filter
        self.png_data = VivaGraph_Js_Views.default(params=[graph_name])


    def test_by_issue_type(self):
        graph_name = 'graph_XKW'    # (7 nodes)
        graph_name = 'graph_MKF'    # ( 20 nodes,  27 edges)

        self.png_data = VivaGraph_Js_Views.by_issue_type(params=[graph_name])

    def test_by_field(self):
        graph_name = 'graph_XKW'    # (7 nodes)
        graph_name = 'graph_MKF'    # ( 20 nodes,  27 edges)
        field      = 'Labels' # ''Rating'
        self.png_data = VivaGraph_Js_Views.by_field(params=[graph_name,field])
        #self.png_data = False

    # def test_people(self):
    #     graph_name = 'graph_CR9'
    #     self.png_data = VivaGraph_Js_Views.people(params=[graph_name],headless=True)

    # bugs

    def test_fixed__bug_graph_doesnt_render(self):
        graph_name = 'graph_AEY'
        graph_name = 'graph_NP5'
        self.png_data = VivaGraph_Js_Views.default(params=[graph_name],headless=True)

    def test_fixed_bug__broken_images(self):
        graph_name = 'graph_34F'
        self.png_data = VivaGraph_Js_Views.default(params=[graph_name],headless=False)



