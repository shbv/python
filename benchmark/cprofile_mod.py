"""
python -m cProfile <script>
or
cProfile.run("<cmd>")
"""

import cProfile
cProfile.run("[i*i for i in range(10000)]")
