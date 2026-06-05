#!/usr/bin/env sh
# Forge requires a configured set of both JVM and program arguments.
# Add custom JVM arguments to the user_jvm_args.txt
# Add custom program arguments {such as nogui} to this file in the next line before the "$@" or
#  pass them to this script directly

# Automatically move client-only mods to a backup folder for server execution
mkdir -p client_mods_backup
for pattern in AmbientSounds BadOptimizations BetterAdvancements BetterModsButton brightnessslider Controlling do_a_barrel_roll dynamic-fps dynamiccrosshair embeddium enhancedvisuals entityculling entity_texture_features entity_model_features fancymenu footprint-particles GeckoLibOculusCompat Highlighter hitindication ImmediatelyFast inventoryhud lootbeams MouseTweaks Night notenoughanimations oculus PresenceFootsteps RyoamicLights skinlayers3d sound-physics-remastered WI-Zoom Xaeros; do
    find mods/ -iname "${pattern}*" -exec mv {} client_mods_backup/ \; 2>/dev/null
done

# Run the server
java @user_jvm_args.txt @libraries/net/minecraftforge/forge/1.20.1-47.4.20/unix_args.txt "$@"

# Restore client-only mods back to mods folder
if [ -d client_mods_backup ]; then
    find client_mods_backup/ -type f -exec mv {} mods/ \; 2>/dev/null
    rm -rf client_mods_backup
fi
