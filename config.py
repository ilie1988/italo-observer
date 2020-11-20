
# LMQ RPC endpoint of italod; can be a unix socket 'ipc:///path/to/italod.sock' (preferred) or a tcp
# socket 'tcp://127.0.0.1:5678'.  Typically you want this running with admin permission.
# This is actually set for each observer in the ...net.py script.
italod_rpc = None

# Default blocks per page for the index.
blocks_per_page=20
# Maximum blocks per page a user can request
max_blocks_per_page=100

# Some display and/or feature options:
pusher=False
key_image_checker=False
output_key_checker=False
autorefresh_option=True
enable_mixins_details=True

# URLs to networks other than the one we are on:
mainnet_url='https://blocks.italonet.dev'
testnet_url='https://testnet.italonet.dev'
devnet_url='https://devnet.italonet.dev'

# Same as above, but these apply if we are on a .italo URL:
italonet_mainnet_url='http://kcpyawm9se7trdbzncimdi5t7st4p5mh9i1mg7gkpuubi4k4ku1y.italo'
italonet_testnet_url='http://testnet.kcpyawm9se7trdbzncimdi5t7st4p5mh9i1mg7gkpuubi4k4ku1y.italo'
italonet_devnet_url='http://devnet.kcpyawm9se7trdbzncimdi5t7st4p5mh9i1mg7gkpuubi4k4ku1y.italo'
