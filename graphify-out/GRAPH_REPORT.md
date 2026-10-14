# Graph Report - Pass-List  (2026-10-14)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 633 nodes · 1818 edges · 23 communities (15 shown, 8 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 215 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Community 0
- Community 1
- Community 2
- Community 3
- Community 4
- Community 5
- Community 6
- Community 7
- Community 8
- Community 9
- Community 10
- Community 11
- Community 12
- Community 13
- Community 14
- Community 15
- Community 16
- Community 17
- Community 18

## God Nodes (most connected - your core abstractions)
1. `log_action()` - 43 edges
2. `FieldDefinition` - 34 edges
3. `Unit` - 30 edges
4. `FieldDefinitionForm` - 28 edges
5. `FieldCondition` - 27 edges
6. `ControllerValuePermissionAndScopeTests` - 26 edges
7. `is_super_admin()` - 26 edges
8. `DropdownOption` - 25 edges
9. `ConditionalFieldTests` - 25 edges
10. `ControllerValuePermissionCompatibilityTests` - 25 edges

## Surprising Connections (you probably didn't know these)
- `FieldDefinitionForm` --uses--> `Unit`  [INFERRED]
  app/core/forms.py → app/core/models.py
- `SearchForm` --uses--> `Unit`  [INFERRED]
  app/core/forms.py → app/core/models.py
- `SecretRecordForm` --uses--> `Unit`  [INFERRED]
  app/core/forms.py → app/core/models.py
- `UnitForm` --uses--> `Unit`  [INFERRED]
  app/core/forms.py → app/core/models.py
- `allowed_units()` --uses--> `Unit`  [INFERRED]
  app/core/security.py → app/core/models.py

## Import Cycles
- None detected.

## Communities (23 total, 8 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.08
Nodes (59): log_action(), AuditLog, Meta, Unit, Meta, admin_units(), is_any_admin(), prepare_request() (+51 more)

### Community 1 - "Community 1"
Cohesion: 0.06
Nodes (37): applicable_field_ids(), condition_data(), controller_values_from_form_data(), normalized(), CaseInsensitiveChoiceField, ControllerFieldChoiceField, ControllerOptionCheckboxWidget, ControllerOptionChoiceField (+29 more)

### Community 2 - "Community 2"
Cohesion: 0.08
Nodes (36): activate_payload(), apply_hostname_payload(), atomic_write(), backup_active(), backup_hostname_runtime(), certificate_metadata(), cleanup_payload_files(), cleanup_stale_staging() (+28 more)

### Community 3 - "Community 3"
Cohesion: 0.05
Nodes (23): get_client_ip(), CaseInsensitiveBackend, blocked_access_response(), ForcePasswordChangeMiddleware, IPAllowlistMiddleware, PerTabAuthenticationMiddleware, BlockedAccessPageSetting, issue_tab_token() (+15 more)

### Community 4 - "Community 4"
Cohesion: 0.08
Nodes (16): decrypt_json(), decrypt_text(), encrypt_json(), encrypt_text(), get_fernet(), ci(), ControllerValuePermission, Meta (+8 more)

### Community 5 - "Community 5"
Cohesion: 0.08
Nodes (18): PanelHostnameForm, Meta, certificate_names(), _dns_pattern_match(), hostname_configuration_hash(), hostname_matches_certificate(), HostRuntimeConfiguration, normalize_hostname() (+10 more)

### Community 6 - "Community 6"
Cohesion: 0.06
Nodes (18): AppSettingForm, Meta, BlockedAccessPageForm, Meta, DropdownOptionForm, Meta, HostnameConfigurationForm, Meta (+10 more)

### Community 7 - "Community 7"
Cohesion: 0.08
Nodes (7): FieldDefinitionForm, Meta, SearchForm, SecretRecordForm, ConditionalFieldTests, ControllerValuePermissionCompatibilityTests, prepare_request()

### Community 8 - "Community 8"
Cohesion: 0.06
Nodes (10): Command, Command, Migration, Migration, Migration, Migration, Migration, Migration (+2 more)

### Community 9 - "Community 9"
Cohesion: 0.13
Nodes (5): RecordFieldValue, Meta, prepare_request(), V110SearchAndDropdownTests, ControllerValuePermissionAndScopeTests

### Community 10 - "Community 10"
Cohesion: 0.12
Nodes (7): IPAllowlistForm, Meta, IPAllowlist, Meta, IPAccessRuleMiddlewareTests, prepare_request(), V19ViewFlowTests

### Community 11 - "Community 11"
Cohesion: 0.22
Nodes (15): activate_candidate(), active_certificate_status(), apply_hostname_configuration(), build_candidate_payload(), CertificateOpsError, cleanup_staged_files(), hostname_configuration_status(), _ops_request() (+7 more)

### Community 12 - "Community 12"
Cohesion: 0.16
Nodes (13): app_branding(), SecurityTimeoutSettingsForm, DynamicSessionTimeoutMiddleware, AppSetting, can_manage_certificates(), can_manage_timeouts(), require_certificate_manager(), wrapper() (+5 more)

### Community 13 - "Community 13"
Cohesion: 0.29
Nodes (8): ensureForcedVisibility(), filterControllerOptions(), optionItem(), parseConditionValues(), refresh(), refreshConditionalForm(), setConditionalRowState(), setRowVisible()

### Community 17 - "Community 17"
Cohesion: 0.83
Nodes (3): currentToken(), ensureFormToken(), urlWithToken()

## Knowledge Gaps
- **8 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `FieldDefinitionForm` connect `Community 7` to `Community 0`, `Community 1`, `Community 4`, `Community 6`, `Community 9`?**
  _High betweenness centrality (0.035) - this node is a cross-community bridge._
- **Are the 20 inferred relationships involving `FieldDefinition` (e.g. with `applicable_field_ids()` and `condition_data()`) actually correct?**
  _`FieldDefinition` has 20 INFERRED edges - model-reasoned connections that need verification._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.07659007659007659 - nodes in this community are weakly interconnected._
- **Why does `FieldDefinition` connect `Community 1` to `Community 0`, `Community 9`, `Community 4`, `Community 7`?**
  _High betweenness centrality (0.029) - this node is a cross-community bridge._
- **Are the 18 inferred relationships involving `Unit` (e.g. with `FieldDefinitionForm` and `SearchForm`) actually correct?**
  _`Unit` has 18 INFERRED edges - model-reasoned connections that need verification._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.06430745814307458 - nodes in this community are weakly interconnected._
- **Why does `IPAllowlist` connect `Community 10` to `Community 0`, `Community 1`, `Community 3`, `Community 4`, `Community 5`?**
  _High betweenness centrality (0.028) - this node is a cross-community bridge._