# -*- coding: utf-8 -*-
#
#  WeeChat-DeaDBeeF  -  WeeChat script for DeaDBeeF integration
#  https://github.com/iceTwy/weechat-deadbeef
#
#  Unless indicated otherwise, files from the WeeChat-DeaDBeeF project 
#  belong to the public domain. Complete license information can be
#  can be found in the LICENSE.md file and at https://unlicense.org.
#
 
SCRIPT_NAME = "deadbeef"
SCRIPT_AUTHOR = "iceTwy"
SCRIPT_VERSION = "0.1"
SCRIPT_LICENSE = "Public Domain"
SCRIPT_DESC = "Controls DeaDBeeF from WeeChat"
DEADBEEF_VERSION = "0.5.6"
deadbeef_version = ''
 
OPTIONS         = { 'deadbeef'         : ('deadbeef','Path to the DeaDBeeF binary file.'),
                    'autostart'        : ('off','Start DeaDBeeF when WeeChat-DeaDBeeF is launched.'),
                    'np.string'        : ('You are listening to:','String appended before the song name when using /db np.'),
                    'saynp.string'     : ('NP:','String appended before the song name when using /db saynp.'),
                    'np.verbose'       : ('%t by %a - from %b (%y)','Verbose arguments when using /db np.'),
                    'saynp.verbose'    : ('%t by %a - from %b (%y)','Verbose arguments when using /db saynp.'),
                    'saynp.me'         : ('off','Send /db saynp with /me (e.g.: /me NP: artist - title)'),
                  }

HOOK   =       { 'script_call_callback': '', 'launch_deadbeef_callback': '', 'control_deadbeef_callback': '' }
 
try:
	import weechat
	IMPORT_OK = True
except ImportError as error:
	IMPORT_OK = False
	if str(error).find('weechat') != -1:
		print('This script must be run under WeeChat.')
		print('Get WeeChat at http://www.weechat.org.')
	else:
		print('There was an error running the DeaDBeeF script for WeeChat.')
                
 
def launch_deadbeef_callback(data, command, rc, out, err):
	'''
	Callback function invoked when the user or the script launches DeaDBeeF.
	Various irrelevant GTK warnings might be returned, so we're not printing the output.
	'''
	
	if int(rc) >= 0:
		if out != "":
			weechat.prnt("", "DeaDBeeF has been successfully closed.")
			
		if err != "" and "starting deadbeef" not in err.strip('\n'):
			if "gtk" not in err.lower():
				weechat.prnt("", "DeaDBeeF script error: %s" % err)
				return weechat.WEECHAT_RC_ERROR
			else:
				pass
	
	if err != "" and "starting deadbeef" not in err.strip('\n'):
		if "gtk" not in err.lower():
			weechat.prnt("", "DeaDBeeF script error: %s" % err)
			return weechat.WEECHAT_RC_ERROR
		else:
			pass
			
	return weechat.WEECHAT_RC_OK
    
def control_deadbeef_callback(data, command, rc, out, err):
	'''
	Callback function invoked when the user types a command.
	Various irrelevant GTK warnings might be returned, so we're not printing the output.
	'''
	
	if not HOOK['launch_deadbeef_callback']:
		weechat.prnt("","DeaDBeeF must be launched in order to run this command.\nPlease use /db launch.")
		return weechat.WEECHAT_RC_OK
	else:
		if int(rc) >= 0:
			if out != "":
				if err != "" and "starting deadbeef" not in err.strip('\n'):
					if "gtk" not in err.lower():
						weechat.prnt("", "DeaDBeeF script error: %s" % err)
						return weechat.WEECHAT_RC_OK
					else:
						pass
				else: 
					if data == "exit":
						weechat.prnt("", "DeaDBeeF has been successfully closed.")
					if data == "play":
						weechat.prnt("", "DeaDBeeF: track playing/reset.")
					if data == "pause":
						weechat.prnt("", "DeaDBeeF: track paused.")
					if data == "stop":
						weechat.prnt("", "DeaDBeeF: track stopped.")
					if data == "next":
						weechat.prnt("", "DeaDBeeF: next track loaded.")
					if data == "prev":
						weechat.prnt("", "DeaDBeeF: previous track loaded.")
					
			elif out == "" and err != "":
				if "gtk" not in err.lower() and "starting deadbeef" not in err.strip('\n'):
					weechat.prnt("", "DeaDBeeF script error: %s" % err)
				else:
					pass
			else:
				if data =="exit":
					weechat.prnt("", "DeaDBeeF has been successfully closed.")
					return weechat.WEECHAT_RC_OK
				else:
					weechat.prnt("", "DeaDBeeF script: the command did not return a value.")
					return weechat.WEECHAT_RC_OK
		else:
			weechat.prnt("", "DeaDBeeF script: the command gave an invalid return code.")
			return weechat.WEECHAT_RC_OK
		
		return weechat.WEECHAT_RC_OK
    
def script_call_callback(data, command, rc, out, err):
	'''
	Callback function invoked when the script itself hooks a process.
	'''
	
	global OPTIONS
	
	if int(rc) >= 0:
		if out != "":
			
			if data == 'grep':
				if int(out) == 0 or int(out) == 1:
					weechat.prnt('', 'DeaDBeeF is not running. Launching...')
					HOOK['launch_deadbeef_callback'] = weechat.hook_process(OPTIONS['deadbeef'], 0, "launch_deadbeef_callback", "launch")
					return weechat.WEECHAT_RC_OK
				elif int(out) > 1:
					weechat.prnt('', 'DeaDBeeF is already running.')
					return weechat.WEECHAT_RC_OK
				else:
					weechat.prnt('', 'DeaDBeeF script: invalid argument/return code while launching DeaDBeeF.')
					return weechat.WEECHAT_RC_OK
					
			if data == 'version':
				deadbeef_version = out
				if DEADBEEF_VERSION in deadbeef_version:
					pass
				else:
					weechat.prnt("", "Your DeaDBeeF version is outdated.\nPlease upgrade to the newest DeaDBeeF version (%s)!" % DEADBEEF_VERSION)
					return weechat.WEECHAT_RC_OK
				
			if data == 'np':
				npstring_eval = weechat.string_eval_expression((weechat.config_string(weechat.config_get("plugins.var.python." + SCRIPT_NAME + ".np.string"))), {}, {}, {})
				weechat.prnt(weechat.current_buffer(), npstring_eval + " %s" % out.strip('\n'))
				
			if data == 'saynp':
				saynpstring_eval = weechat.string_eval_expression((weechat.config_string(weechat.config_get("plugins.var.python." + SCRIPT_NAME + ".saynp.string"))), {}, {}, {})
				saynpstring_sent = weechat.string_remove_color(saynpstring_eval, "")
				if OPTIONS['saynp.me'] == 'on':
					weechat.command(weechat.current_buffer(), "/me " + saynpstring_sent + " %s" % out.strip('\n'))
					return weechat.WEECHAT_RC_OK
				else:
					weechat.command(weechat.current_buffer(), saynpstring_sent + " %s" % out.strip('\n'))
					return weechat.WEECHAT_RC_OK
					
			else:
				if err != "" and "starting deadbeef" not in err.strip('\n'):
					if "gtk" not in err.lower():
						weechat.prnt("", "DeaDBeeF script error: %s" % err)
					else:
						pass
		else:
			if err != "" and "starting deadbeef" not in err.strip('\n'):
				if "gtk" not in err.lower():
					weechat.prnt("", "DeaDBeeF script error: %s" % err)
				else:
					pass
					
	else:
		if err != "" and "starting deadbeef" not in err.strip('\n'):
			if "gtk" not in err.lower():
				weechat.prnt("", "DeaDBeeF script error: %s" % err)
			else:
				pass
				
	return weechat.WEECHAT_RC_OK
 
def is_deadbeef_running():
	'''
	Checks if DeaDBeeF is running or not, and launches it if it isn't.
	'''
	
	global HOOK, OPTIONS
	
	if OPTIONS['autostart'] == "on":
		HOOK['script_call_callback'] = weechat.hook_process('pgrep -c deadbeef', 1000, "script_call_callback", "grep")
		return weechat.WEECHAT_RC_OK
	else:
		pass
		return weechat.WEECHAT_RC_OK
		
        return weechat.WEECHAT_RC_OK
                        
def check_deadbeef_version():
	'''
	Checks the current DeaDBeeF version.
	'''
	
	global HOOK,OPTIONS
	
	HOOK['script_call_callback'] = weechat.hook_process(OPTIONS['deadbeef'] + ' --version', 1000, "script_call_callback", "version") 
	return weechat.WEECHAT_RC_OK
 
def search_hook(ptr_hook,name):
	'''
	Searches if a hook is active by looking for its pointer. Essentially, the goal is to cope with
	DeaDBeeF's slow response times by avoiding hooking another process if one is already running -
	in this case, the output of the process is incorrect.
	'''
	
	global HOOK
	
	if ptr_hook:
		infolist = weechat.infolist_get('hook',ptr_hook,'')
		weechat.infolist_free(infolist)
		#weechat.prnt("","infolist: %s" % infolist) #debug info
		if infolist:
			#weechat.prnt("","hook: name %s pointer: %s found.." % (name, ptr_hook)) #debug info
			return 0
			
	#weechat.prnt("","hook: name %s pointer: %s not found.." % (name, ptr_hook)) #debug info
	HOOK[name] = ''
	return 1
 
def deadbeef(data,buffer,args):
	
	global HOOK,OPTIONS
	
	args = args.split(' ')
	
	if args[0].lower() == 'launch':
		if search_hook(HOOK['launch_deadbeef_callback'],'launch_deadbeef_callback'):
			HOOK['launch_deadbeef_callback'] = weechat.hook_process(OPTIONS['deadbeef'], 0, "launch_deadbeef_callback", "")
			
	elif args[0].lower() == 'exit':
		if search_hook(HOOK['control_deadbeef_callback'],'control_deadbeef_callback'):
			HOOK['control_deadbeef_callback'] = weechat.hook_process('pkill deadbeef', 1000, "control_deadbeef_callback", "exit")
			
	elif args[0].lower() == 'play':
		if search_hook(HOOK['control_deadbeef_callback'],'control_deadbeef_callback'):
			HOOK['control_deadbeef_callback'] = weechat.hook_process(OPTIONS['deadbeef'] + " --play", 1000, "control_deadbeef_callback", "play")
			weechat.prnt('', 'DeaDBeeF: playing/reset track.')
	
	elif args[0].lower() == 'pause':
		if search_hook(HOOK['control_deadbeef_callback'],'control_deadbeef_callback'):
			HOOK['control_deadbeef_callback'] =  weechat.hook_process(OPTIONS['deadbeef'] + " --pause", 1000, "control_deadbeef_callback", "pause")
			weechat.prnt('', 'DeaDBeeF: track paused/resumed.')
			
	elif args[0].lower() == 'stop':
		if search_hook(HOOK['control_deadbeef_callback'],'control_deadbeef_callback'):
			HOOK['control_deadbeef_callback'] = weechat.hook_process(OPTIONS['deadbeef'] + " --stop", 1000, "control_deadbeef_callback", "stop")
			weechat.prnt('', 'DeaDBeeF: track stopped.')
			
	elif args[0].lower() == 'next':
		if search_hook(HOOK['control_deadbeef_callback'],'control_deadbeef_callback'):
			HOOK['control_deadbeef_callback'] = weechat.hook_process(OPTIONS['deadbeef'] + " --next", 1000, "control_deadbeef_callback", "next")
			weechat.prnt('', 'DeaDBeeF: next track loaded.')
			
	elif args[0].lower() == 'prev':
		if search_hook(HOOK['control_deadbeef_callback'],'control_deadbeef_callback'):
			HOOK['control_deadbeef_callback'] = weechat.hook_process(OPTIONS['deadbeef'] + " --prev", 1000, "control_deadbeef_callback", "prev")
			weechat.prnt('', 'DeaDBeeF: previous track loaded.')
			
	elif args[0].lower() == 'np':
		npverbose_eval = weechat.string_eval_expression((weechat.config_string(weechat.config_get("plugins.var.python." + SCRIPT_NAME + ".np.verbose"))), {}, {}, {})
		if search_hook(HOOK['script_call_callback'],'script_call_callback'):
			HOOK['script_call_callback'] = weechat.hook_process(OPTIONS['deadbeef'] + ' --nowplaying ' + '"' + npverbose_eval + '"', 1000, "script_call_callback", "np")
			
	elif args[0].lower() == 'saynp':
		saynpverbose_eval = weechat.string_eval_expression((weechat.config_string(weechat.config_get("plugins.var.python." + SCRIPT_NAME + ".saynp.verbose"))), {}, {}, {})
		saynpverbose_sent = weechat.string_remove_color(saynpverbose_eval, "")
		if search_hook(HOOK['script_call_callback'],'script_call_callback'):
			HOOK['script_call_callback'] = weechat.hook_process(OPTIONS['deadbeef'] + ' --nowplaying ' + '"' + saynpverbose_sent + '"', 1000, "script_call_callback", "saynp")
			
	return weechat.WEECHAT_RC_OK
 
# ================================[ weechat options & description ]===============================
def init_options():
	for option,value in OPTIONS.items():
		if not weechat.config_is_set_plugin(option):
			weechat.config_set_plugin(option, value[0])
			OPTIONS[option] = value[0]
		else:
			OPTIONS[option] = weechat.config_get_plugin(option)
		weechat.config_set_desc_plugin(option, '%s (default: "%s")' % (value[1], value[0]))
 
def toggle_refresh(pointer, name, value):
	global OPTIONS
	option = name[len('plugins.var.python.' + SCRIPT_NAME + '.'):]        # get optionname
	OPTIONS[option] = value                                               # save new value
	return weechat.WEECHAT_RC_OK
 
 
if __name__ == '__main__' and IMPORT_OK and weechat.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION, SCRIPT_LICENSE, SCRIPT_DESC, '', ''):
	
	version = weechat.info_get("version_number", "") or 0
	if int(version) >= 0x00040200: # 0.4.2
		init_options()
		is_deadbeef_running()
		check_deadbeef_version()
		weechat.prnt('', 'DeaDBeeF script loaded successfully!')
		weechat.hook_command("db", "DeaDBeeF control features & now-playing", "[launch] | [np] | [saynp] | [play] | [pause] | [next] | [prev] | [stop] | [exit]","""
		launch: launches DeaDBeeF if an instance is not already running
		np: indicates the track that is being played
		saynp: says the track that is being played in the current buffer
		play: plays a track/resumes to selected track if a track is already running
		pause: pauses track
		next: skips to next track in playlist
		prev: skips to previous track in playlist
		stop: stops playback of the current track
		exit: exits DeaDBeeF
		""", "np|saynp|launch|play|pause|next|prev|stop|exit", "deadbeef", "")
		
		weechat.hook_config( 'plugins.var.python.' + SCRIPT_NAME + '.*', 'toggle_refresh', '' )
		
	else:
		weechat.prnt("","%s%s %s" % (weechat.prefix("error"),SCRIPT_NAME,": requires WeeChat version 0.4.2 or higher."))
		weechat.command("","/wait 1ms /python unload %s" % SCRIPT_NAME)            
