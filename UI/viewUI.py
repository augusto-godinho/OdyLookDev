import bpy

class ODYLOOKDEV_PT_view_panel_settings(bpy.types.Panel):
    """Creates a Panel in the view 3d properties window"""
    bl_label = "Character Settings"
    bl_idname = "view_panel_settings"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Odyssey'

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        odylookdev = scene.odylookdev
        
        panel = layout.column()
        
        panel.label(text="Character")
        panel.prop(odylookdev,'character_name')
        panel.prop(odylookdev,'character_skin')
        panel.prop(odylookdev,'character_has_recolor')
        if odylookdev.character_has_recolor:
            panel.prop(odylookdev,'character_recolor')
            
        panel.prop(odylookdev,'has_diff_root_folder')
        if odylookdev.has_diff_root_folder:
            panel.prop(odylookdev,'root_folder')
        panel.label(text="")
        panel.prop(odylookdev,'light_rotation')
        panel.prop(odylookdev,'light_z')
        panel.prop(odylookdev,'rim_color')
        panel.prop(odylookdev,'rim_intensity')

class ODYLOOKDEV_PT_view_panel_actions(bpy.types.Panel):
    """Creates a Panel in the view 3d properties window"""
    bl_label = "Operations"
    bl_idname = "view_panel_actions"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Odyssey'

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        odylookdev = scene.odylookdev
        
        panel = layout.column()
        panel.label(text="Clean up")
        box = layout.column()
        clean_panel = box.box()
        clean_panel.operator("odylookdev.clean_duplicated_nodes")

        panel = layout.column()
        panel.label(text="Export")
        box = layout.column()
        export_box = box.box()
        export_box.operator("odylookdev.export_materials")
        export_box.operator("odylookdev.export_main")
        export_box.operator("odylookdev.export_with_outline")

#>>>------PANEL DRAWER------->
class ODYLOOKDEV_PT_view_panel_Outline(bpy.types.Panel):
    bl_label = "Ody Outline"
    bl_idname = "view_panel_outline"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_category = "Odyssey"
    
    def draw(self, context):
        layout = self.layout
        
        
        col = layout.column()
        col.operator("odylookdev.add_outline")
        col.operator("odylookdev.export_as_outline")
        
        col.label(text="Thickness")
        row = col.row()
        row.alignment = 'EXPAND'
        row.operator("odylookdev.vertex_aplha", text="ADD").flow = "ADD"
        row.operator("odylookdev.vertex_aplha", text="REMOVE").flow = "REMOVE"



class ODYLOOKDEV_PT_object_panel(bpy.types.Panel):
    bl_label = "Odyssey"
    bl_idname = "Odyssey_object_panel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout

        obj = context.object
        scene = context.scene
        
        row = layout.row()
        row.prop(obj, "vertex_position_bake")