import bpy

#object properties
#bpy.types.Object.lightmap_group = bpy.props.IntProperty(name="Lightmap Group")

class OdyLookDevProperties(bpy.types.PropertyGroup):
    def update_light_rotation(self, context):
        bpy.data.node_groups.get('Light Direction').nodes.get('LightRotation').outputs[0].default_value = self.light_rotation
    def update_light_z(self, context):
        bpy.data.node_groups.get('Light Direction').nodes.get('LightZ').outputs[0].default_value = self.light_z

    character_name : bpy.props.StringProperty(name='Name', description='Character name related to this file', default='Character_Name')
    character_skin : bpy.props.StringProperty(name='Skin', description='Character skin name related to this file',  default='Skin_Name')
    character_recolor : bpy.props.StringProperty(name='Recolor', description='Character skin recolor name related to this file',  default='Recolor_Name')
    character_has_recolor : bpy.props.BoolProperty(name='Recolor', description='Character skin recolor name related to this file',  default=False)
    light_rotation : bpy.props.FloatProperty(name='Light Rotation', description='The main light rotation in the scene',  default=-2, update=update_light_rotation)
    light_z : bpy.props.FloatProperty(name='Light Z', description='The main light rotation Z in the scene',  default=0.5, update=update_light_z)
    
    

#scene properties


def register():
    """
    This function registers the property group class and adds it to the window manager context when the
    addon is enabled.
    """
    bpy.utils.register_class(OdyLookDevProperties)
    bpy.types.Scene.odylookdev = bpy.props.PointerProperty(type=OdyLookDevProperties)
    


def unregister():
    """
    This function unregisters the property group class and deletes it from the window manager context when the
    addon is disabled.
    """
    bpy.utils.unregister_class(OdyLookDevProperties)
    del bpy.types.Scene.odylookdev