# Initialize parent node variable.
if locals().get("hou_parent") is None:
    hou_parent = hou.node("/obj/geo1")

# Code for /obj/geo1/test1
hou_node = hou_parent.createNode("subnet", "test1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-13.2964, -6.78785))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/test1/label1 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1")
hou_parm = hou_node.parm("label1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("Sub-Network Input #1")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/label2 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1")
hou_parm = hou_node.parm("label2")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("Sub-Network Input #2")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/label3 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1")
hou_parm = hou_node.parm("label3")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("Sub-Network Input #3")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/label4 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1")
hou_parm = hou_node.parm("label4")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("Sub-Network Input #4")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "18.5.672")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("18.5.672")
# Update the parent node.
hou_parent = hou_node

# Code for /obj/geo1/test1/output0
hou_node = hou_parent.createNode("output", "output0", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(1.14229, 1.1253))
hou_node.bypass(False)
hou_node.setDisplayFlag(True)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(True)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/test1/output0/outputidx parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/output0")
hou_parm = hou_node.parm("outputidx")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "18.5.672")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("18.5.672")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/test1/sphere1
hou_node = hou_parent.createNode("sphere", "sphere1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(2.32477, 4.57544))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/test1/sphere1/type parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/sphere1")
hou_parm = hou_node.parm("type")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("poly")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/sphere1/surftype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/sphere1")
hou_parm = hou_node.parm("surftype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("quads")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/sphere1/rad parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/sphere1")
hou_parm_tuple = hou_node.parmTuple("rad")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((1, 1, 1))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/test1/sphere1/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/sphere1")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/test1/sphere1/r parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/sphere1")
hou_parm_tuple = hou_node.parmTuple("r")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/test1/sphere1/scale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/sphere1")
hou_parm = hou_node.parm("scale")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/sphere1/orient parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/sphere1")
hou_parm = hou_node.parm("orient")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("y")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/sphere1/freq parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/sphere1")
hou_parm = hou_node.parm("freq")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(2)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/sphere1/rows parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/sphere1")
hou_parm = hou_node.parm("rows")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(13)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/sphere1/cols parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/sphere1")
hou_parm = hou_node.parm("cols")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(24)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/sphere1/orderu parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/sphere1")
hou_parm = hou_node.parm("orderu")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(4)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/sphere1/orderv parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/sphere1")
hou_parm = hou_node.parm("orderv")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(4)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/sphere1/imperfect parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/sphere1")
hou_parm = hou_node.parm("imperfect")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/sphere1/upole parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/sphere1")
hou_parm = hou_node.parm("upole")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/sphere1/accurate parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/sphere1")
hou_parm = hou_node.parm("accurate")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/sphere1/triangularpoles parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/sphere1")
hou_parm = hou_node.parm("triangularpoles")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "18.5.672")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("18.5.672")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/test1/subdivide1
hou_node = hou_parent.createNode("subdivide", "subdivide1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(2.32477, 3.2031))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/test1/subdivide1/subdivide parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/subdivide1")
hou_parm = hou_node.parm("subdivide")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/subdivide1/creases parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/subdivide1")
hou_parm = hou_node.parm("creases")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/subdivide1/algorithm parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/subdivide1")
hou_parm = hou_node.parm("algorithm")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("osdcc")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/subdivide1/iterations parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/subdivide1")
hou_parm = hou_node.parm("iterations")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(2)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/subdivide1/overridecrease parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/subdivide1")
hou_parm = hou_node.parm("overridecrease")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/subdivide1/creaseweight parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/subdivide1")
hou_parm = hou_node.parm("creaseweight")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/subdivide1/outputcrease parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/subdivide1")
hou_parm = hou_node.parm("outputcrease")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/subdivide1/outcreasegroup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/subdivide1")
hou_parm = hou_node.parm("outcreasegroup")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("creases")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/subdivide1/closeholes parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/subdivide1")
hou_parm = hou_node.parm("closeholes")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("pull")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/subdivide1/surroundpoly parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/subdivide1")
hou_parm = hou_node.parm("surroundpoly")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("edges")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/subdivide1/bias parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/subdivide1")
hou_parm = hou_node.parm("bias")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/subdivide1/updatenmls parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/subdivide1")
hou_parm = hou_node.parm("updatenmls")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/subdivide1/smoothvertex parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/subdivide1")
hou_parm = hou_node.parm("smoothvertex")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/subdivide1/consisttopology parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/subdivide1")
hou_parm = hou_node.parm("consisttopology")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/subdivide1/linearcreases parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/subdivide1")
hou_parm = hou_node.parm("linearcreases")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/subdivide1/buildpolysoups parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/subdivide1")
hou_parm = hou_node.parm("buildpolysoups")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/subdivide1/indepcurves parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/subdivide1")
hou_parm = hou_node.parm("indepcurves")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/subdivide1/removeholes parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/subdivide1")
hou_parm = hou_node.parm("removeholes")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/subdivide1/vtxboundary parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/subdivide1")
hou_parm = hou_node.parm("vtxboundary")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("corner")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/subdivide1/fvarlinear parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/subdivide1")
hou_parm = hou_node.parm("fvarlinear")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("corner1")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/subdivide1/creasemethod parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/subdivide1")
hou_parm = hou_node.parm("creasemethod")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("uniform")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/subdivide1/trianglesubd parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/subdivide1")
hou_parm = hou_node.parm("trianglesubd")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("catclark")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "18.5.672")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("18.5.672")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/test1/attribwrangle1
hou_node = hou_parent.createNode("attribwrangle", "attribwrangle1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(1.51692, 2.1632))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/test1/attribwrangle1/folder01 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/attribwrangle1")
hou_parm = hou_node.parm("folder01")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/attribwrangle1/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/attribwrangle1")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/attribwrangle1/grouptype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/attribwrangle1")
hou_parm = hou_node.parm("grouptype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("guess")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/attribwrangle1/class parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/attribwrangle1")
hou_parm = hou_node.parm("class")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("point")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/attribwrangle1/vex_numcount parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/attribwrangle1")
hou_parm = hou_node.parm("vex_numcount")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(10)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/attribwrangle1/vex_threadjobsize parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/attribwrangle1")
hou_parm = hou_node.parm("vex_threadjobsize")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1024)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/attribwrangle1/snippet parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/attribwrangle1")
hou_parm = hou_node.parm("snippet")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("@Cd = {1, 0, 0};")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/attribwrangle1/exportlist parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/attribwrangle1")
hou_parm = hou_node.parm("exportlist")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/attribwrangle1/vex_strict parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/attribwrangle1")
hou_parm = hou_node.parm("vex_strict")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/attribwrangle1/autobind parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/attribwrangle1")
hou_parm = hou_node.parm("autobind")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/attribwrangle1/bindings parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/attribwrangle1")
hou_parm = hou_node.parm("bindings")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/attribwrangle1/groupautobind parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/attribwrangle1")
hou_parm = hou_node.parm("groupautobind")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/attribwrangle1/groupbindings parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/attribwrangle1")
hou_parm = hou_node.parm("groupbindings")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/attribwrangle1/vex_cwdpath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/attribwrangle1")
hou_parm = hou_node.parm("vex_cwdpath")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(".")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/attribwrangle1/vex_outputmask parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/attribwrangle1")
hou_parm = hou_node.parm("vex_outputmask")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/attribwrangle1/vex_updatenmls parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/attribwrangle1")
hou_parm = hou_node.parm("vex_updatenmls")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/attribwrangle1/vex_matchattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/attribwrangle1")
hou_parm = hou_node.parm("vex_matchattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("id")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/attribwrangle1/vex_inplace parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/attribwrangle1")
hou_parm = hou_node.parm("vex_inplace")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/attribwrangle1/vex_selectiongroup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/attribwrangle1")
hou_parm = hou_node.parm("vex_selectiongroup")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/test1/attribwrangle1/vex_precision parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/test1/attribwrangle1")
hou_parm = hou_node.parm("vex_precision")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("auto")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code to establish connections for /obj/geo1/test1/output0
hou_node = hou_parent.node("output0")
if hou_parent.node("attribwrangle1") is not None:
    hou_node.setInput(0, hou_parent.node("attribwrangle1"), 0)
# Code to establish connections for /obj/geo1/test1/subdivide1
hou_node = hou_parent.node("subdivide1")
if hou_parent.node("sphere1") is not None:
    hou_node.setInput(0, hou_parent.node("sphere1"), 0)
# Code to establish connections for /obj/geo1/test1/attribwrangle1
hou_node = hou_parent.node("attribwrangle1")
if hou_parent.node("subdivide1") is not None:
    hou_node.setInput(0, hou_parent.node("subdivide1"), 0)

# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

