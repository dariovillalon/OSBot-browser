import base64
import json
import unittest
from   unittest import TestCase

from osbot_browser.browser.Browser_Commands import Browser_Commands
from pbx_gs_python_utils.utils.Dev import Dev
from pbx_gs_python_utils.utils.Files import Files

from gw_bot.Deploy import Deploy


class Test_Browser_Commands(TestCase):

    def setUp(self):
        self.browser_commands = Browser_Commands()
        self.png_file         = '/tmp/lambda_png_file.png'
        self.team_id          = 'T7F3AUXGV'
        self.channel          = 'DDKUZTK6X' #''GDL2EC3EE'
        self.result           = None

    def tearDown(self):
        if self.result is not None:
            Dev.pprint(self.result)

    def _save_png_data(self, png_data):
        png_file = '/tmp/lambda_png_file.png'
        if png_data:
            with open(png_file, "wb") as fh:
                fh.write(base64.decodebytes(png_data.encode()))

    def test_list(self):
        result = self.browser_commands.list(None, None, None)
        assert result[0] == 'Here are the current examples files:'
        assert len(result[1][0].get('text').split('\n')) > 10
        #assert result == (, [{'text': ''}])


    def test_screenshot(self):
        #os.environ['OSX_CHROME'] = 'True'
        url = 'https://www.google.co.uk'
        self.browser_commands.screenshot(self.team_id, self.channel, [url])

    def test_slack(self):
        #os.environ['OSX_CHROME'] = 'True'
        params = ['random', 2000]
        self.result = self.browser_commands.slack(self.team_id, self.channel, params)

    @unittest.skip("needs server running locally")
    def test_screenshot__localhost(self):
        url = 'http://localhost:12345'
        png_data = self.browser_commands.screenshot(None, None, params = [url])
        self._save_png_data(png_data)

    @unittest.skip("has delay")
    def test_screenshot__with_delay(self):
        url   = "https://www.google.com"
        delay = 2
        png_data = self.browser_commands.screenshot(None, None, params=[url,delay])
        self._save_png_data(png_data)

    def test_render(self):
        params   = ['examples/wardley_map/cup-of-tea.html']
        png_data = self.browser_commands.render(None,None,params)

        Files.delete(self.png_file)
        self._save_png_data(png_data)
        assert Files.exists(self.png_file)

    @unittest.skip('hangs')
    def test_render__with_clip_params(self):
        #params = ['/examples/bootstrap-cdn.html'        ,0  ,0 ,500 ,50 ]
        params = ['examples/wardley_map/cup-of-tea.html',250,50,600 ,200]
        png_data = self.browser_commands.render(None,None,params)
        Files.delete(self.png_file)
        self._save_png_data(png_data)
        assert Files.exists(self.png_file)

    @unittest.skip('has delay')
    def test_render_with_delay(self):
        params   = ['go-js','2']
        png_data = self.browser_commands.render(None,None,params)
        #Dev.print(png_data)
        self._save_png_data(png_data)

    def test_markdown___no_params(self):
        result = self.browser_commands.markdown(None,None,None)
        self._save_png_data(result)
        #Dev.pprint(result)

    def test_markdown___with_params(self):
        params = ["# Created from unit test \n","2nd paragraph --- 123"]
        result = self.browser_commands.markdown(None,None,params)
        self._save_png_data(result)

    def test_risk(self):
        params = ['GSSP-6']
        params = ['GSSP-113']
        result = self.browser_commands.risks(params=params)
        self._save_png_data(result)

    def test_graph(self):
        graph_name = 'graph_XKW'
        params = [graph_name,'default']
        result = self.browser_commands.graph(params=params)
        Dev.pprint(result)
        self._save_png_data(result)

    def test_graph__view__node_label(self):
        graph_name = 'graph_DEQ'
        params = [graph_name,'node_label', 'Labels']
        result = self.browser_commands.graph(params=params)
        Dev.pprint(result)
        self._save_png_data(result)

    def test_am_charts(self):
        graph_name = 'graph_XKW'
        params = [graph_name,'default']
        result = self.browser_commands.am_charts(params=params)
        Dev.pprint(result)
        self._save_png_data(result)

    def test_viva_graph(self):
        graph_name = 'graph_XKW'
        graph_name = 'graph_7AN' # 74 nodes
        #graph_name = 'graph_HDS' # very large graph
        #graph_name = 'graph_37V' # with `1617` nodes and `2907` edges,
        #graph_name = 'graph_VQW'
        graph_name = 'graph_56M'
        params = [graph_name,'default']
        result = self.browser_commands.viva_graph(params=params)
        #Dev.pprint(result)
        self._save_png_data(result)

    def test_go_js(self):
        graph_name = 'graph_XKW'
        params = [graph_name,'default']
        result = self.browser_commands.go_js(params=params)
        Dev.pprint(result)
        self._save_png_data(result)


    def test_table(self):
        params =['issue','GSOS-181']
        result = self.browser_commands.table(params=params)
        Dev.pprint(result)

    def test_google_charts(self):
        Deploy().setup()

        channel = 'DJ8UA0RFT'
        self.browser_commands.google_charts(None, channel,['default'])
        #self.browser_commands.oss_today(None, channel)

    def test_sow(self):
        result = self.browser_commands.sow(None, None,['default'])
        Dev.pprint(result)
        #self.browser_commands.oss_today(None, channel)


    def test_deploy(self):
        Deploy().setup().deploy_lambda__browser()