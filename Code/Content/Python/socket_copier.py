import unreal


def copy_sockets_from_to(source_path: str, target_paths: list, overwrite: bool = False) -> dict:
    result = {"success": [], "errors": [], "skipped": []}

    # --- Charger la source ---
    source_mesh = unreal.load_asset(source_path)
    if not source_mesh or not isinstance(source_mesh, unreal.StaticMesh):
        unreal.log_error(f"[SocketCopier] Source introuvable : {source_path}")
        result["errors"].append(source_path)
        return result

    source_sockets = source_mesh.get_sockets_by_tag("")
    if not source_sockets:
        unreal.log_warning(f"[SocketCopier] Aucune socket sur la source : {source_path}")
        return result

    unreal.log(f"[SocketCopier] Source : {source_path}  |  {len(source_sockets)} socket(s)")

    # --- Traiter chaque cible ---
    for target_path in target_paths:
        target_mesh = unreal.load_asset(target_path)
        if not target_mesh or not isinstance(target_mesh, unreal.StaticMesh):
            unreal.log_error(f"[SocketCopier] Cible introuvable : {target_path}")
            result["errors"].append(target_path)
            continue

        copied = 0
        skipped = 0

        for src in source_sockets:
            name = src.socket_name

            # Vérifier si la socket existe déjà
            existing = target_mesh.find_socket(name)
            if existing:
                if not overwrite:
                    skipped += 1
                    continue
                else:
                    target_mesh.remove_socket(existing)

            # ✅ set_editor_property pour les champs read-only
            new_socket = unreal.StaticMeshSocket()
            new_socket.set_editor_property("socket_name",       name)
            new_socket.set_editor_property("relative_location", src.relative_location)
            new_socket.set_editor_property("relative_rotation", src.relative_rotation)
            new_socket.set_editor_property("relative_scale",    src.relative_scale)
            new_socket.set_editor_property("tag",               src.tag)

            target_mesh.add_socket(new_socket)
            copied += 1

        unreal.EditorAssetLibrary.save_asset(target_path)

        log_msg = f"✓ {target_path}  →  {copied} copiée(s)"
        if skipped:
            log_msg += f", {skipped} ignorée(s) (doublon)"
        unreal.log(f"[SocketCopier] {log_msg}")
        result["success"].append(target_path)

    unreal.log(f"[SocketCopier] Terminé. {len(result['success'])} OK, {len(result['errors'])} erreur(s).")
    return result


# ─────────────────────────────────────────────────────────────
#  CONFIG — modifie les chemins ici
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":

    SOURCE_MESH = "/Game/Assets/Build/Stylized/Wood/SM_Wood_Ramp"

    TARGET_MESHES = [
        "/Game/Assets/Build/Stylized/Metal/SM_Metal_Ramp",
        "/Game/Assets/Build/Stylized/Stone/SM_Stone_Ramp",
    ]

    copy_sockets_from_to(SOURCE_MESH, TARGET_MESHES, overwrite=True)