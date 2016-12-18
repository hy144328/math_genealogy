# Copyright (C) 2016  Hans Yu
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#!/usr/bin/env python

from stammbaum import *

# settings
max_level = 5

# parent
student_ident = 149678
student_name = 'Matthew P. Juniper'

g = Stammbaum(max_level)

student_node = Node(student_ident, student_name)
g.set_advisors(student_node, 0)
#for m in mathematicians:
#    print mathematicians[m]
