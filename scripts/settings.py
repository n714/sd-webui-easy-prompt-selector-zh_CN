from modules import script_callbacks, shared

def on_ui_settings():
    shared.opts.add_option("eps_enable_save_raw_prompt_to_pnginfo", shared.OptionInfo(False, "Save original prompt to pngninfo", section=("easy_prompt_selector", "EasyPromptSelector")))

script_callbacks.on_ui_settings(on_ui_settings)
