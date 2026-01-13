# SENAITE Archetypes → Dexterity Migration Analysis

## Executive Summary

The final blocker for SENAITE Python 3 support is the migration from **Products.Archetypes** to **Plone Dexterity**. Archetypes is Python 2 only and cannot be installed in Python 3 environments. This analysis examines the scope of the migration and provides a roadmap for implementation.

## Current Archetypes Usage in SENAITE

### Core Dependencies
- **Products.Archetypes** - Content type framework (Python 2 only)
- **Products.ATContentTypes** - Archetypes content types
- **Archetypes-based schemas** - Field definitions and validation

### Files Affected
**Total: 219 files mention "Archetypes" across the codebase**

Key areas:
- `src/bika/lims/__init__.py` - Core content type registration
- `src/bika/lims/content/` - 100+ content type definitions
- `src/senaite/core/patches/archetypes/` - Archetypes patches
- `src/senaite/core/browser/widgets/` - Archetypes widgets
- `src/senaite/core/browser/fields/` - Archetypes fields

## The Migration Challenge

### What Archetypes Provides
1. **Content Type Definitions** - Schema-based content types
2. **Field Types** - StringField, IntegerField, ReferenceField, etc.
3. **Widgets** - UI components for field editing
4. **Validation** - Field validation and constraints
5. **Catalog Integration** - Automatic indexing
6. **Migration Framework** - Data migration between versions

### Dexterity Equivalents
1. **Content Types** → Dexterity FTI (Factory Type Information)
2. **Schema Fields** → zope.schema fields
3. **Widgets** → z3c.form widgets
4. **Validation** → zope.schema constraints
5. **Catalog** → Custom catalog integration
6. **Migration** → Custom migration scripts

## Migration Scope Assessment

### Phase 1: Core Infrastructure (High Priority)
**Estimated: 2-3 months development**

#### Content Type Registration
**File:** `src/bika/lims/__init__.py`
**Current:**
```python
from Products.Archetypes.atapi import listTypes, process_types
content_types, constructors, ftis = process_types(listTypes(PROJECTNAME), PROJECTNAME)
```

**Target:**
```python
# Register Dexterity content types
from plone.dexterity import content
# Manual registration of each content type
```

#### Schema Migration
**Files:** `src/bika/lims/content/*.py` (100+ files)

**Current Archetypes Schema:**
```python
schema = Organisation.schema.copy() + Schema((
    StringField("ClientID", required=1, ...),
    ReferenceField("PrimaryContact", ...),
    ...
))
```

**Target Dexterity Schema:**
```python
from zope import schema
from plone.autoform import directives
from plone.supermodel import model

class IClient(model.Schema):
    client_id = schema.TextLine(
        title=u"Client ID",
        required=True,
        ...
    )
    primary_contact = RelationChoice(
        title=u"Primary Contact",
        ...
    )
```

### Phase 2: Field Types Migration (Medium Priority)
**Estimated: 1-2 months**

#### Widget Migration
- Archetypes widgets → z3c.form widgets
- Custom field types → Dexterity behaviors
- Validation logic → zope.schema constraints

#### Catalog Integration
- Archetypes auto-indexing → Manual catalog registration
- Custom indexes → plone.indexer decorators
- Search functionality → Custom search adapters

### Phase 3: Data Migration (High Priority)
**Estimated: 1 month**

#### Content Migration
- Archetypes objects → Dexterity objects
- Field data preservation
- Reference integrity
- Workflow state migration

#### Upgrade Scripts
- GenericSetup profile updates
- Migration handlers
- Rollback capabilities

## Implementation Strategy

### Step 1: Parallel Development
1. **Keep Archetypes branch** for production
2. **Create Dexterity branch** for development
3. **Dual maintenance** during transition

### Step 2: Incremental Migration
1. **Start with simple content types** (Client, Contact, etc.)
2. **Migrate complex types** (AnalysisRequest, Sample)
3. **Update dependent code** after each migration

### Step 3: Testing Strategy
1. **Unit tests** for each migrated type
2. **Integration tests** for workflows
3. **Performance testing** for catalog operations
4. **Data migration testing** with real datasets

## Technical Challenges

### 1. Custom Field Types
SENAITE has many custom field types:
- `MultiUploadField` - File uploads
- `UIDReferenceField` - Internal references
- `RecordsField` - Complex data structures
- `DurationField` - Time durations

**Solution:** Create Dexterity equivalents or use behaviors.

### 2. Complex Schemas
Many content types inherit and extend schemas:
```python
schema = Organisation.schema.copy() + Schema((...))
```

**Solution:** Convert to proper Dexterity inheritance.

### 3. Dynamic Fields
SENAITE allows dynamic field configuration through the web interface.

**Solution:** Implement dynamic schema modification in Dexterity.

### 4. Catalog Performance
Archetypes provides automatic indexing. Dexterity requires manual catalog configuration.

**Solution:** Comprehensive catalog setup with proper indexes.

## Resource Requirements

### Development Team
- **2-3 Senior Plone/Dexterity Developers**
- **1-2 SENAITE Domain Experts**
- **QA Engineer** for testing

### Timeline Estimates
- **Phase 1 (Infrastructure):** 2-3 months
- **Phase 2 (Fields/Widgets):** 1-2 months
- **Phase 3 (Data Migration):** 1 month
- **Testing & Stabilization:** 1-2 months

**Total: 5-8 months for complete migration**

### Risk Mitigation
- **Parallel maintenance** of both branches
- **Incremental rollout** with feature flags
- **Comprehensive testing** before production deployment
- **Rollback procedures** for data migration

## Alternative Approaches

### Option 1: Archetypes Python 3 Port (Not Recommended)
- Attempt to make Archetypes Python 3 compatible
- **Cons:** Massive undertaking, upstream resistance, ongoing maintenance burden
- **Pros:** Preserves existing architecture

### Option 2: Partial Migration (Recommended)
- Migrate core content types to Dexterity
- Keep legacy types in Archetypes with Python 2 compatibility layer
- **Pros:** Incremental approach, reduced risk
- **Cons:** Mixed architecture complexity

### Option 3: Framework Replacement
- Consider modern alternatives (Django, FastAPI + React)
- **Pros:** Clean slate, modern architecture
- **Cons:** Complete rewrite, loss of Plone ecosystem

## Current Status Assessment

### ✅ Completed (Our Work)
- Python 3 packaging infrastructure
- Syntax compatibility fixes
- Development environment setup
- Migration documentation

### ⏳ Next Steps (Community Effort)
1. **Create Dexterity migration branch**
2. **Start with Client content type migration**
3. **Establish migration patterns**
4. **Community coordination for large-scale effort**

## Recommendations

### Immediate Actions
1. **Create dedicated Dexterity migration branch**
2. **Form migration working group** with Plone/Dexterity experts
3. **Start with proof-of-concept** on simple content types
4. **Document migration patterns** for community contribution

### Long-term Strategy
1. **Maintain Archetypes branch** for production stability
2. **Incremental Dexterity migration** with feature flags
3. **Community-driven development** with clear milestones
4. **Comprehensive testing** before production rollout

## Success Criteria

### Technical Success
- ✅ All content types migrated to Dexterity
- ✅ Data migration preserves integrity
- ✅ Performance meets or exceeds Archetypes
- ✅ All existing functionality preserved

### Community Success
- ✅ Clear documentation for future maintainers
- ✅ Migration patterns established
- ✅ Testing framework comprehensive
- ✅ Rollback procedures documented

---

## Conclusion

The Archetypes → Dexterity migration represents the final major hurdle for SENAITE Python 3 support. While technically challenging, it follows established Plone migration patterns and can be accomplished with proper planning and community coordination.

The foundation work completed in this PR demonstrates that the Python 3 ecosystem is ready. The Dexterity migration is primarily an architectural modernization effort that will position SENAITE for long-term maintainability and feature development.

**Priority: HIGH** - This migration unlocks the full potential of modern Python development for SENAITE.

---

*Analysis completed: January 13, 2026*
*Prepared by: Python 3 Upgrade Initiative*