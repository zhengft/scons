#!/usr/bin/env python
#
# __COPYRIGHT__
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

__revision__ = "__FILE__ __REVISION__ __DATE__ __DEVELOPER__"

"""
Verify that an Action list with a string command containing a Unicode file
name, and a Python function action, works corectly.  This verifies that
the signatures of the two actions can be concatenated without encoding
Unicode problems.
"""

import TestSCons

test = TestSCons.TestSCons()

try:
    unicode
except NameError:
    import sys
    msg = "Unicode not supported by Python version %s; skipping test\n"
    test.skip_test(msg % sys.version[:3])

test.write('SConstruct', """
fnode = File(u'foo.txt')

def funcact(target, source, env):
    open(str(target[0]), 'wb').write("funcact\\n")
    for i in range(300):
        pass
    return 0

env = Environment()

env.Command(fnode, [], ["echo $TARGET", funcact])
""")

test.run(arguments = '.')

test.must_match('foo.txt', "funcact\n")

test.up_to_date(arguments = '.')

test.pass_test()

# Local Variables:
# tab-width:4
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=4 shiftwidth=4:
