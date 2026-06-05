@echo off
REM Forge requires a configured set of both JVM and program arguments.
REM Add custom JVM arguments to the user_jvm_args.txt
REM Add custom program arguments {such as nogui} to this file in the next line before the %* or
REM  pass them to this script directly

REM Automatically move client-only mods to a backup folder for server execution
if not exist client_mods_backup mkdir client_mods_backup
for %%p in (AmbientSounds BadOptimizations BetterAdvancements BetterModsButton brightnessslider Controlling do_a_barrel_roll dynamic-fps dynamiccrosshair embeddium enhancedvisuals entityculling entity_texture_features entity_model_features fancymenu footprint-particles GeckoLibOculusCompat Highlighter hitindication ImmediatelyFast inventoryhud lootbeams MouseTweaks Night notenoughanimations oculus PresenceFootsteps RyoamicLights skinlayers3d sound-physics-remastered WI-Zoom Xaeros e4mc) do (
    move "mods\*%%p*" client_mods_backup\ >nul 2>&1
)

REM Run the server
java @user_jvm_args.txt @libraries/net/minecraftforge/forge/1.20.1-47.4.20/win_args.txt %*

REM Restore client-only mods back to mods folder
if exist client_mods_backup (
    move client_mods_backup\* mods\ >nul 2>&1
    rmdir client_mods_backup >nul 2>&1
)

pause
