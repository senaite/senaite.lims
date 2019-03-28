from OFS.ObjectManager import ObjectManager

ADD_SENAITE_SITE = """
<dtml-if expr="_.len(this().getPhysicalPath()) == 1 and len(objectValues('Plone Site')) == 0">
</dtml-if>
<dtml-if expr="_.len(this().getPhysicalPath()) == 1 and len(objectValues('Plone Site')) > 0">
  <!-- Add Plone site action-->
  <style type="text/css">
   .form { margin: 1em auto; text }
   .button { padding: 6px 12px; background-color: #337ab7; color: #fff; }
  </style>
  <form class="form"
        method="get"
        action="&dtml-URL1;/@@senaite-addsite"
        target="_top">
    <input type="hidden" name="site_id" value="senaite" />
    <input class="button" type="submit" value="Add SENAITE Site" />
  </form>
</dtml-if>
"""

main = ObjectManager.manage_main
orig = main.read()
pos = orig.find('<!-- Add object widget -->')


# Add in our button html at the right position
new = orig[:pos] + ADD_SENAITE_SITE + orig[pos:]

# Modify the manage_main
main.edited_source = new
main._v_cooked = main.cook()
