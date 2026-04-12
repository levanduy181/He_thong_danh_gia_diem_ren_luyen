import { createContext, useContext, useMemo, useReducer, useState, createElement, useEffect } from "react"
import { applyDelta, ReflexEvent, hydrateClientStorage, useEventLoop, refs } from "$/utils/state"
import { jsx } from "@emotion/react";

export const initialState = {"reflex___state____state": {"is_hydrated_rx_state_": false, "router_rx_state_": {"session": {"client_token": "", "client_ip": "", "session_id": ""}, "headers": {"host": "", "origin": "", "upgrade": "", "connection": "", "cookie": "", "pragma": "", "cache_control": "", "user_agent": "", "sec_websocket_version": "", "sec_websocket_key": "", "sec_websocket_extensions": "", "accept_encoding": "", "accept_language": "", "raw_headers": {}}, "page": {"host": "", "path": "", "raw_path": "", "full_path": "", "full_raw_path": "", "params": {}}, "url": "", "route_id": ""}}, "reflex___state____state.ptit_reflex___state____conduct_state": {"active_tab_rx_state_": "student_info", "admin_event_criterion_choice_rx_state_": "", "admin_new_event_end_time_rx_state_": "", "admin_new_event_location_rx_state_": "", "admin_new_event_name_rx_state_": "", "admin_new_event_points_rx_state_": "1", "admin_new_event_semester_id_rx_state_": 0, "admin_new_event_semester_name_rx_state_": "", "admin_new_event_start_time_rx_state_": "", "admin_stage_0_end_rx_state_": "", "admin_stage_0_label_rx_state_": "", "admin_stage_0_start_rx_state_": "", "admin_stage_1_end_rx_state_": "", "admin_stage_1_label_rx_state_": "", "admin_stage_1_start_rx_state_": "", "admin_stage_2_end_rx_state_": "", "admin_stage_2_label_rx_state_": "", "admin_stage_2_start_rx_state_": "", "admin_stage_3_end_rx_state_": "", "admin_stage_3_label_rx_state_": "", "admin_stage_3_start_rx_state_": "", "advisor_gpa_input_rx_state_": "", "advisor_note_rx_state_": "", "auth_mode_rx_state_": "login", "can_create_evidence_rx_state_": false, "can_download_conduct_pdf_rx_state_": false, "can_edit_advisor_note_rx_state_": false, "can_edit_class_note_rx_state_": false, "can_edit_own_profile_rx_state_": false, "can_edit_student_gpa_rx_state_": false, "can_edit_student_note_rx_state_": false, "can_reset_submission_rx_state_": false, "can_review_advisor_rx_state_": false, "can_review_class_rx_state_": false, "can_save_class_rx_state_": false, "can_save_student_rx_state_": false, "can_submit_student_rx_state_": false, "class_note_rx_state_": "", "column_config_open_rx_state_": false, "conduct_grade_label_rx_state_": "—", "criterion_choice_ids_rx_state_": [], "criterion_choice_labels_rx_state_": [], "current_user_class_name_rx_state_": "", "current_user_email_rx_state_": "", "current_user_faculty_rx_state_": "", "current_user_initial_rx_state_": "", "current_user_name_rx_state_": "", "current_user_role_rx_state_": "", "current_user_role_label_rx_state_": "", "current_user_student_code_rx_state_": "", "event_modal_open_rx_state_": false, "event_tab_rx_state_": "joined", "evidence_activity_content_rx_state_": "", "evidence_award_level_rx_state_": "", "evidence_categories_rx_state_": [], "evidence_city_rx_state_": "", "evidence_count_rx_state_": "0", "evidence_detail_open_rx_state_": false, "evidence_district_rx_state_": "", "evidence_dormitory_rx_state_": "", "evidence_event_name_rx_state_": "", "evidence_file_name_rx_state_": "", "evidence_grid_columns_rx_state_": "64px 160px 220px 160px 180px 180px minmax(200px, 1fr)", "evidence_host_name_rx_state_": "", "evidence_host_phone_rx_state_": "", "evidence_modal_open_rx_state_": false, "evidence_participation_time_rx_state_": "", "evidence_residence_type_rx_state_": "Ngoại trú", "evidence_room_number_rx_state_": "", "evidence_rows_rx_state_": [], "evidence_share_time_rx_state_": "", "evidence_social_type_rx_state_": "", "evidence_street_address_rx_state_": "", "evidence_url_rx_state_": "", "evidence_ward_rx_state_": "", "filtered_role_management_rows_rx_state_": [], "filtered_students_rx_state_": [], "flash_kind_rx_state_": "info", "flash_message_rx_state_": "", "flash_token_rx_state_": 0, "grading_target_banner_text_rx_state_": "", "has_evidence_rows_rx_state_": false, "has_filtered_role_management_rows_rx_state_": false, "has_open_events_rx_state_": false, "has_registered_events_rx_state_": false, "is_authenticated_rx_state_": false, "joined_events_rx_state_": [], "loading_rx_state_": true, "login_error_rx_state_": "", "login_password_rx_state_": "", "login_username_rx_state_": "", "main_info_sidebar_label_rx_state_": "Thông tin sinh viên", "nav_students_open_rx_state_": true, "nav_students_parent_active_rx_state_": false, "open_events_rx_state_": [], "outside_window_rx_state_": true, "profile_edit_address_rx_state_": "", "profile_edit_birth_date_rx_state_": "", "profile_edit_email_rx_state_": "", "profile_edit_full_name_rx_state_": "", "profile_edit_gender_rx_state_": "", "profile_edit_phone_rx_state_": "", "profile_editing_rx_state_": false, "register_address_rx_state_": "", "register_birth_date_rx_state_": "", "register_class_name_rx_state_": "", "register_email_rx_state_": "", "register_faculty_rx_state_": "", "register_faculty_options_rx_state_": ["An toàn thông tin", "Công nghệ thông tin", "Điện tử viễn thông", "Truyền thông đa phương tiện"], "register_full_name_rx_state_": "", "register_gender_rx_state_": "", "register_gender_options_rx_state_": ["Nam", "Nữ", "Khác"], "register_major_rx_state_": "", "register_major_options_rx_state_": [], "register_password_rx_state_": "", "register_password_confirm_rx_state_": "", "register_phone_rx_state_": "", "register_student_code_rx_state_": "", "register_username_rx_state_": "", "registered_events_rx_state_": [], "role_management_class_groups_rx_state_": [], "role_management_classes_rx_state_": [], "role_management_has_selection_rx_state_": false, "role_management_rows_rx_state_": [], "score_effective_total_rx_state_": "0", "score_rows_rx_state_": [], "score_total_rx_state_": "0", "score_total_advisor_rx_state_": "0", "score_total_class_rx_state_": "0", "selected_account_id_rx_state_": 0, "selected_event_rx_state_": {}, "selected_event_counts_to_score_rx_state_": "", "selected_event_end_time_rx_state_": "", "selected_event_location_rx_state_": "", "selected_event_name_rx_state_": "", "selected_event_note_rx_state_": "", "selected_event_start_time_rx_state_": "", "selected_event_type_label_rx_state_": "", "selected_evidence_can_advisor_review_rx_state_": false, "selected_evidence_can_class_review_rx_state_": false, "selected_evidence_category_rx_state_": "special_achievement", "selected_evidence_category_label_rx_state_": "Thành tích đặc biệt", "selected_evidence_detail_rx_state_": {}, "selected_evidence_fields_rx_state_": [], "selected_evidence_status_label_rx_state_": "", "selected_evidence_title_rx_state_": "", "selected_role_management_class_rx_state_": "", "selected_semester_id_rx_state_": 0, "selected_semester_is_active_rx_state_": false, "selected_semester_name_rx_state_": "", "selected_student_class_rx_state_": "", "selected_student_code_rx_state_": "", "selected_student_id_rx_state_": 0, "selected_student_label_rx_state_": "", "selected_student_name_rx_state_": "", "semester_names_rx_state_": [], "semesters_rx_state_": [], "show_action_col_rx_state_": true, "show_class_col_rx_state_": true, "show_declaration_tabs_rx_state_": false, "show_full_name_col_rx_state_": true, "show_reporter_col_rx_state_": true, "show_role_management_tab_rx_state_": false, "show_self_score_tab_rx_state_": false, "show_status_col_rx_state_": true, "show_student_code_col_rx_state_": true, "show_student_directory_tab_rx_state_": false, "show_students_events_tab_rx_state_": false, "show_students_evidence_tab_rx_state_": false, "show_students_score_tab_rx_state_": false, "student_directory_sidebar_label_rx_state_": "Danh sách sinh viên", "student_labels_rx_state_": [], "student_list_filter_rx_state_": "", "student_note_rx_state_": "", "student_profile_rx_state_": {}, "students_rx_state_": [], "submission_status_rx_state_": "", "submission_status_label_rx_state_": "", "timeline_rx_state_": []}, "reflex___state____state.reflex___state____frontend_event_exception_state": {}, "reflex___state____state.reflex___state____on_load_internal_state": {}, "reflex___state____state.reflex___state____update_vars_internal_state": {}}

export const defaultColorMode = "system"
export const ColorModeContext = createContext(null);
export const UploadFilesContext = createContext(null);
export const DispatchContext = createContext(null);
export const StateContexts = {reflex___state____state: createContext(null),reflex___state____state__ptit_reflex___state____conduct_state: createContext(null),reflex___state____state__reflex___state____frontend_event_exception_state: createContext(null),reflex___state____state__reflex___state____on_load_internal_state: createContext(null),reflex___state____state__reflex___state____update_vars_internal_state: createContext(null),};
export const EventLoopContext = createContext(null);
export const clientStorage = {"cookies": {}, "local_storage": {}, "session_storage": {}}


export const state_name = "reflex___state____state"

export const exception_state_name = "reflex___state____state.reflex___state____frontend_event_exception_state"

// These events are triggered on initial load and each page navigation.
export const onLoadInternalEvent = () => {
    const internal_events = [];

    // Get tracked cookie and local storage vars to send to the backend.
    const client_storage_vars = hydrateClientStorage(clientStorage);
    // But only send the vars if any are actually set in the browser.
    if (client_storage_vars && Object.keys(client_storage_vars).length !== 0) {
        internal_events.push(
            ReflexEvent(
                'reflex___state____state.reflex___state____update_vars_internal_state.update_vars_internal',
                {vars: client_storage_vars},
            ),
        );
    }

    // `on_load_internal` triggers the correct on_load event(s) for the current page.
    // If the page does not define any on_load event, this will just set `is_hydrated = true`.
    internal_events.push(ReflexEvent('reflex___state____state.reflex___state____on_load_internal_state.on_load_internal'));

    return internal_events;
}

// The following events are sent when the websocket connects or reconnects.
export const initialEvents = () => [
    ReflexEvent('reflex___state____state.hydrate'),
    ...onLoadInternalEvent()
]
    

export const isDevMode = true;

export function UploadFilesProvider({ children }) {
  const [filesById, setFilesById] = useState({})
  refs["__clear_selected_files"] = (id) => setFilesById(filesById => {
    const newFilesById = {...filesById}
    delete newFilesById[id]
    return newFilesById
  })
  return createElement(
    UploadFilesContext.Provider,
    { value: [filesById, setFilesById] },
    children
  );
}

export function ClientSide(component) {
  return ({ children, ...props }) => {
    const [Component, setComponent] = useState(null);
    useEffect(() => {
      async function load() {
        const comp = await component();
        setComponent(() => comp);
      }
      load();
    }, []);
    return Component ? jsx(Component, props, children) : null;
  };
}

export function EventLoopProvider({ children }) {
  const dispatch = useContext(DispatchContext)
  const [addEvents, connectErrors] = useEventLoop(
    dispatch,
    initialEvents,
    clientStorage,
  )
  return createElement(
    EventLoopContext.Provider,
    { value: [addEvents, connectErrors] },
    children
  );
}

export function StateProvider({ children }) {
  const [reflex___state____state, dispatch_reflex___state____state] = useReducer(applyDelta, initialState["reflex___state____state"])
const [reflex___state____state__ptit_reflex___state____conduct_state, dispatch_reflex___state____state__ptit_reflex___state____conduct_state] = useReducer(applyDelta, initialState["reflex___state____state.ptit_reflex___state____conduct_state"])
const [reflex___state____state__reflex___state____frontend_event_exception_state, dispatch_reflex___state____state__reflex___state____frontend_event_exception_state] = useReducer(applyDelta, initialState["reflex___state____state.reflex___state____frontend_event_exception_state"])
const [reflex___state____state__reflex___state____on_load_internal_state, dispatch_reflex___state____state__reflex___state____on_load_internal_state] = useReducer(applyDelta, initialState["reflex___state____state.reflex___state____on_load_internal_state"])
const [reflex___state____state__reflex___state____update_vars_internal_state, dispatch_reflex___state____state__reflex___state____update_vars_internal_state] = useReducer(applyDelta, initialState["reflex___state____state.reflex___state____update_vars_internal_state"])
  const dispatchers = useMemo(() => {
    return {
      "reflex___state____state": dispatch_reflex___state____state,
"reflex___state____state.ptit_reflex___state____conduct_state": dispatch_reflex___state____state__ptit_reflex___state____conduct_state,
"reflex___state____state.reflex___state____frontend_event_exception_state": dispatch_reflex___state____state__reflex___state____frontend_event_exception_state,
"reflex___state____state.reflex___state____on_load_internal_state": dispatch_reflex___state____state__reflex___state____on_load_internal_state,
"reflex___state____state.reflex___state____update_vars_internal_state": dispatch_reflex___state____state__reflex___state____update_vars_internal_state,
    }
  }, [])

  return (
    createElement(StateContexts.reflex___state____state,{value: reflex___state____state},
createElement(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state,{value: reflex___state____state__ptit_reflex___state____conduct_state},
createElement(StateContexts.reflex___state____state__reflex___state____frontend_event_exception_state,{value: reflex___state____state__reflex___state____frontend_event_exception_state},
createElement(StateContexts.reflex___state____state__reflex___state____on_load_internal_state,{value: reflex___state____state__reflex___state____on_load_internal_state},
createElement(StateContexts.reflex___state____state__reflex___state____update_vars_internal_state,{value: reflex___state____state__reflex___state____update_vars_internal_state},
    createElement(DispatchContext, {value: dispatchers}, children)
    )))))
  )
}