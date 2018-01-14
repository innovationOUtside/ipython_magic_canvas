DEFAULT_CONTEXT = 'ctx'
class Canvas(object):
    def __init__(self,script,cid='mytag', context=None):
        self.cid=cid
        self.context = context if context else DEFAULT_CONTEXT
        self.wrap =  context is None
        self._html =[]
        self._add_canvas(cid)
        self._get_canvas()
        self._add_script_tag(script)
        
    def _add_canvas(self, cid):
        html='''<canvas id="{}" width="700" height="410">  <p>Some default content can appear here.</p>
</canvas>'''.format(cid)
        self._html.append(html)
        
    def _get_canvas(self):
        script = '''<script type="text/javascript">var canvas = document.getElementById('{cid}');
  //if (canvas.getContext) {{}}
    var {ctx} = canvas.getContext('2d');</script> '''.format(cid = self.cid, ctx=self.context)
        self._html.append(script)
    
    def _add_script_tag(self, script):
        if self.wrap:
            self._html.append('<script type="text/javascript">with ({}) {{ {} }}</script>'.format(self.context,script))
        else:
            self._html.append('<script type="text/javascript">{}</script>'.format(script))

    def html(self):
        return '\n'.join(self._html)
        
    def _repr_html_(self):
        return self.html()


import random
import string
import shlex
from argparse import ArgumentParser
from IPython.core.magic import (
    magics_class, line_cell_magic, Magics)
from IPython.core.display import HTML

@magics_class
class CanvasMagic(Magics):
    def __init__(self, shell, cache_display_data=False):
        super(CanvasMagic, self).__init__(shell)
        self.cache_display_data = cache_display_data

    @line_cell_magic
    def canvas(self,line, cell=''):
        '''Run JS canvas commands.'''
        parser = ArgumentParser()
        parser.add_argument('-c', '--context', default=None)
        parser.add_argument('-I', '--id', default=None)
        parser.add_argument('--wrap', dest='wrap_env', action='store_true')
        parser.add_argument('-v', '--variable', default=None)
        parser.set_defaults(wrap_env=False)
        args = parser.parse_args(shlex.split(line))
        
        if args.variable:
            cell = self.shell.user_ns[args.variable]
  
        #Create a random id for the canvas tag to try to prevent clashes
        argsid = args.id if args.id else ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
            
        if not args.context:
            if not args.wrap_env: context = None
            else: context=DEFAULT_CONTEXT
        else: context = args.context
        #We need to add the extra \n in case the last line in the cell is a comment that would comment out </script>
        return Canvas(cell+'\n', context=context, cid=argsid)

#ip = get_ipython()
#ip.register_magics(CanvasMagic)