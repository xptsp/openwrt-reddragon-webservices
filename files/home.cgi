#!/usr/bin/lua
uci  = require "luci.model.uci".cursor()
ucis = require "luci.model.uci".cursor_state()
compress = true
compressed = ""
uci:load('nginx')
uci:load('webservices')

------------------------------------------------------------
--- Necessary functions for our code:
------------------------------------------------------------
function file_exists(name)
	local f=io.open(name,"r")
	if f~=nil then io.close(f) return true else return false end
end
function wprint(s)
	if compress then
		compressed = compressed .. s:match( "^%s*(.-)%s*$" )
	else
		print(s)
	end
end
function toInt(number, default)
    return math.floor(tonumber(number) or default)
end

------------------------------------------------------------
--- Get number of grid elements we have:
------------------------------------------------------------
elements = 0
old_compress = compress
compress = true
uci:foreach('nginx', 'server', function(s)
	if s['include'] == 'reverse_proxy' then		
		comment = string.match(s['location'], '#.*')
		comment = comment:gsub('\#', '')
		filename = '/icons/' .. s['.name'] .. '.svg'
		if not file_exists('/www' .. filename) then
			filename = '/icons/' .. s['.name'] .. '.png'
		end
		wprint('			<div><a target="_blank" href="https://' .. s["server_name"] .. '"><img src="' .. filename .. '" /><p>' .. comment .. '</p></a></div>')
		elements = elements +1
	end
end)
uci:foreach('webservices', 'redirect', function(s)
	filename = '/icons/' .. s['.name'] .. '.svg'
	if not file_exists('/www' .. filename) then
		filename = '/icons/' .. s['.name'] .. '.png'
	end
	wprint('			<div><a target="_blank" href="' .. s['location'] .. '"><img src="' .. filename .. '" /><p>' .. s['comment'] .. '</p></a></div>')
	elements = elements +1
end)
compress = old_compress
grid_data = compressed
compressed = ""

------------------------------------------------------------
--- Retrieve our Web Services configuration:
------------------------------------------------------------
title = uci:get('webservices', 'config', 'title') or 'Available Services'
desktop_columns = toInt(uci:get('webservices', 'config', 'desktop_columns'), 4)
mobile_columns = toInt(uci:get('webservices', 'config', 'mobile_columns'), 3)
background_image = uci:get('webservices', 'config', 'background_image') or '/luci-static/argon/img/bg1.jpg'
background_color = uci:get('webservices', 'config', 'background_color') or '000000'

------------------------------------------------------------
--- Output the entire HTML block
------------------------------------------------------------
print('Content-type: Text/html')
print('')
wprint('<!DOCTYPE html>')
wprint('<html lang="en">')
wprint('<head>')
wprint('	<title>' .. title .. '</title>')
wprint('	<meta name="viewport" content="width=device-width, initial-scale=1.0"> ')
wprint(' 	<meta http-equiv="content-type" content="text/html; charset=UTF-8">')
wprint('	<meta charset="UTF-8">')
wprint('	<style>')
wprint('		body {')
wprint('			background-color:#' .. background_color .. ';')
wprint('			background-image:url(' .. background_image .. ');')
wprint('			-webkit-background-size: cover;')
wprint('			-moz-background-size: cover;')
wprint('			-o-background-size: cover;')
wprint('			background-size: cover;')
wprint('			min-height: 100vh;')
wprint('			background-repeat: no-repeat;')
wprint('			background-attachment: fixed;')
wprint('			background-size: 100% 100%;')
wprint('			box-sizing: border-box;')
wprint('			display: flex;')
wprint('			align-items: top;')
wprint('			justify-content: center;')
wprint('			color: white;')
wprint('		}')
wprint('		.title {')
wprint('			text-align: center;')					
wprint('			display: block;')
wprint('		}')
wprint('		.grid {')
wprint('			flex: 0 0 auto;')
wprint('			perspective: 600px;')
wprint('			display: grid;')
wprint('			grid-template-columns: repeat(' .. desktop_columns .. ', 192px);')
wprint('			grid-template-rows: repeat(' .. math.ceil(elements / desktop_columns) .. ', 192px);')
wprint('			grid-gap: 15px;')
wprint('			max-width: 4600px;')
wprint('		}')
wprint('		.grid div {')
wprint('			background: rgba(255, 255, 255, 0.25);')
wprint('			border: 1px solid rgba(255, 255, 255, 0.25);')
wprint('			padding: 10px;')
wprint('			color: white;')
wprint('			box-shadow: 30px 30px 30px -20px rgba(0, 0, 0, 0.6);')
wprint('			border-radius: 12px;')
wprint('		}')
wprint('		.grid div img {')
wprint('			width: 128px;')
wprint('			height: 128px;')
wprint('			display: block;')
wprint('			margin-left: auto;')
wprint('			margin-right: auto;')
wprint('		}')
wprint('		.grid div a {')
wprint('			color: white;')
wprint('			text-align: center;')
wprint('			text-decoration: none;')
wprint('			text-align:center;')
wprint('		}')
wprint('		.grid div p {')
wprint('			text-align:center;')
wprint('			text-overflow: ellipsis;')
wprint('			white-space: nowrap;')
wprint('			overflow: hidden;')
wprint('		}')
wprint('		@media (max-width: 800px) {')
wprint('			.grid {')
wprint('				grid-template-columns: repeat(' .. mobile_columns .. ', 135px);')
wprint('				grid-template-rows: repeat(' .. math.ceil(elements / mobile_columns) .. ', 150px);')
wprint('				grid-gap: 10px;')
wprint('			}')
wprint('			.grid div img {')
wprint('				width: 96px;')
wprint('				height: 96px;')
wprint('			}')
wprint('		}')
wprint('	</style>')
wprint('	<script>')
wprint('		window.console = window.console || function(t) {};')
wprint('	</script> ')
wprint('</head>')
wprint('<body translate="no">')
wprint('	<div class="title">')
wprint('		<div class="title">')
wprint('			<p><h1>' .. title .. '</h1></p>')
wprint('		</div>')
wprint('		<div class="grid">' .. grid_data .. '</div>')
wprint('	</div>')
wprint('</body></html>')
print(compressed)
