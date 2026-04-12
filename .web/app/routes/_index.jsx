import {Fragment,useCallback,useContext,useEffect,useRef} from "react"
import {EventLoopContext,StateContexts} from "$/utils/context"
import {ReflexEvent,isNotNullOrUndefined,isTrue,refs} from "$/utils/state"
import {Box as RadixThemesBox,Button as RadixThemesButton,Flex as RadixThemesFlex,Grid as RadixThemesGrid,Link as RadixThemesLink,Select as RadixThemesSelect,Text as RadixThemesText,TextArea as RadixThemesTextArea,TextField as RadixThemesTextField} from "@radix-ui/themes"
import DebounceInput from "react-debounce-input"
import {} from "react-dropzone"
import {useDropzone} from "react-dropzone"
import {Link as ReactRouterLink} from "react-router"
import {jsx} from "@emotion/react"




function Text_3f94262ab772c69001ae97d04536acbb () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : "white", ["fontWeight"] : "700", ["fontSize"] : "18px" })},reflex___state____state__ptit_reflex___state____conduct_state.current_user_initial_rx_state_)
  )
}


function Text_74cb1db8d6e4754970e3e4fb18ce7ba8 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["color"] : "#1f2937", ["fontWeight"] : "600" })},reflex___state____state__ptit_reflex___state____conduct_state.current_user_name_rx_state_)
  )
}


function Text_0e9abb9cdd5f5895fe50d99a3850f0e9 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280" })},reflex___state____state__ptit_reflex___state____conduct_state.current_user_student_code_rx_state_)
  )
}


function Fragment_9d7fa90aa05a72acbf78a4fc85c81116 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(!((reflex___state____state__ptit_reflex___state____conduct_state.current_user_student_code_rx_state_?.valueOf?.() === ""?.valueOf?.()))?(jsx(Fragment,{},jsx(Text_0e9abb9cdd5f5895fe50d99a3850f0e9,{},))):(jsx(Fragment,{},))))
  )
}


function Text_2351b54af388b792761e6d24fb6636ed () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["fontWeight"] : "700", ["color"] : "white" })},reflex___state____state__ptit_reflex___state____conduct_state.current_user_role_label_rx_state_)
  )
}


function Button_24bda2e046077ade6297da2e52fb3438 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_d541d88e53836082a6663939a7066d63 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.logout", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : "white", ["color"] : "#1f2937", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:on_click_d541d88e53836082a6663939a7066d63},"\u0110\u0103ng xu\u1ea5t")
  )
}


function Text_0c5f92c81173d118ff303d3317ac9cca () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : ((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "student_info"?.valueOf?.()) ? "white" : "#374151"), ["fontSize"] : "14px", ["fontWeight"] : ((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "student_info"?.valueOf?.()) ? "700" : "500"), ["lineHeight"] : "1.45" })},reflex___state____state__ptit_reflex___state____conduct_state.main_info_sidebar_label_rx_state_)
  )
}


function Box_ccca5db63ccdc5eca9b4aabacc0f7d72 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_5a350c7139897f7a4e986241b524eacd = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.select_tab", ({ ["tab"] : "student_info" }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesBox,{css:({ ["padding"] : "12px 14px", ["borderRadius"] : "8px", ["background"] : ((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "student_info"?.valueOf?.()) ? "#d92314" : "transparent"), ["cursor"] : "pointer", ["width"] : "100%" }),onClick:on_click_5a350c7139897f7a4e986241b524eacd},jsx(Text_0c5f92c81173d118ff303d3317ac9cca,{},))
  )
}


function Text_2e374bf575714260e77334393efc4372 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : ((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "role_management"?.valueOf?.()) ? "white" : "#374151"), ["fontSize"] : "14px", ["fontWeight"] : ((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "role_management"?.valueOf?.()) ? "700" : "500"), ["lineHeight"] : "1.45" })},"Qu\u1ea3n l\u00fd t\u00e0i kho\u1ea3n")
  )
}


function Box_128170947a5c34d2ae569928622d8d60 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_9197288e79df701354bbb60243212544 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.select_tab", ({ ["tab"] : "role_management" }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesBox,{css:({ ["padding"] : "12px 14px", ["borderRadius"] : "8px", ["background"] : ((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "role_management"?.valueOf?.()) ? "#d92314" : "transparent"), ["cursor"] : "pointer", ["width"] : "100%" }),onClick:on_click_9197288e79df701354bbb60243212544},jsx(Text_2e374bf575714260e77334393efc4372,{},))
  )
}


function Fragment_33dd63420e035ae96c5826441651aaba () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.show_role_management_tab_rx_state_?(jsx(Fragment,{},jsx(Box_128170947a5c34d2ae569928622d8d60,{},))):(jsx(Fragment,{},))))
  )
}


function Text_93357265ef575d23b77f9e403c932508 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : ((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "admin_conduct_timeline"?.valueOf?.()) ? "white" : "#374151"), ["fontSize"] : "14px", ["fontWeight"] : ((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "admin_conduct_timeline"?.valueOf?.()) ? "700" : "500"), ["lineHeight"] : "1.45" })},"M\u1ed1c th\u1eddi gian \u0111\u00e1nh gi\u00e1")
  )
}


function Box_23906e4e609bbf97e123433f6215a084 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_14152bc068e3242ec039fa1223eda927 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.select_tab", ({ ["tab"] : "admin_conduct_timeline" }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesBox,{css:({ ["padding"] : "12px 14px", ["borderRadius"] : "8px", ["background"] : ((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "admin_conduct_timeline"?.valueOf?.()) ? "#d92314" : "transparent"), ["cursor"] : "pointer", ["width"] : "100%" }),onClick:on_click_14152bc068e3242ec039fa1223eda927},jsx(Text_93357265ef575d23b77f9e403c932508,{},))
  )
}


function Fragment_0f79e807b6fa303e5172a125c10f5305 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},((reflex___state____state__ptit_reflex___state____conduct_state.current_user_role_rx_state_?.valueOf?.() === "admin"?.valueOf?.())?(jsx(Fragment,{},jsx(Box_23906e4e609bbf97e123433f6215a084,{},))):(jsx(Fragment,{},))))
  )
}


function Text_b2018e5d48bd0e67460e476d15f3cce3 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["fontWeight"] : (reflex___state____state__ptit_reflex___state____conduct_state.nav_students_parent_active_rx_state_ ? "700" : "600"), ["color"] : (reflex___state____state__ptit_reflex___state____conduct_state.nav_students_parent_active_rx_state_ ? "white" : "#374151") })},reflex___state____state__ptit_reflex___state____conduct_state.student_directory_sidebar_label_rx_state_)
  )
}


function Box_606e47821c1668eb627d7c918023f09d () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_b7ad4d3a8049a1a34a889eafe985392c = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.open_students_list", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesBox,{css:({ ["flex"] : "1", ["padding"] : "12px 8px 12px 14px", ["cursor"] : "pointer" }),onClick:on_click_b7ad4d3a8049a1a34a889eafe985392c},jsx(Text_b2018e5d48bd0e67460e476d15f3cce3,{},))
  )
}


function Text_ef2d6cdbe410bce352e42207b527b7a1 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700" })},(reflex___state____state__ptit_reflex___state____conduct_state.nav_students_open_rx_state_ ? "\u25be" : "\u25b8"))
  )
}


function Box_228ccccb66176ca9a675c97401e5d1a2 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_bd569843ff401e44c601221ecd54cb88 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.toggle_students_nav", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesBox,{css:({ ["padding"] : "12px 10px", ["cursor"] : "pointer" }),onClick:on_click_bd569843ff401e44c601221ecd54cb88},jsx(Text_ef2d6cdbe410bce352e42207b527b7a1,{},))
  )
}


function Flex_687716799a134450add4d34227032395 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["borderRadius"] : "8px", ["background"] : (reflex___state____state__ptit_reflex___state____conduct_state.nav_students_parent_active_rx_state_ ? "#d92314" : "transparent") }),direction:"row",gap:"0"},jsx(Box_606e47821c1668eb627d7c918023f09d,{},),jsx(Box_228ccccb66176ca9a675c97401e5d1a2,{},))
  )
}


function Text_28a0453ca2a9db0c577594bf99b6efeb () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : (((((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_score_list"?.valueOf?.()) || (true && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_score"?.valueOf?.()))) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_evidence"?.valueOf?.()))) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_events"?.valueOf?.()))) ? "white" : "#4b5563"), ["fontSize"] : "13px", ["fontWeight"] : (((((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_score_list"?.valueOf?.()) || (true && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_score"?.valueOf?.()))) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_evidence"?.valueOf?.()))) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_events"?.valueOf?.()))) ? "700" : "500"), ["lineHeight"] : "1.45" })},"Duy\u1ec7t phi\u1ebfu \u0111i\u1ec3m r\u00e8n luy\u1ec7n")
  )
}


function Box_d8863f0d003c7d4672865f4f883831d1 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_84b72b6a8e0b8388ef06f5a059622e2f = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.select_tab", ({ ["tab"] : "students_score_list" }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesBox,{css:({ ["padding"] : "8px 12px 8px 28px", ["borderRadius"] : "8px", ["background"] : (((((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_score_list"?.valueOf?.()) || (true && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_score"?.valueOf?.()))) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_evidence"?.valueOf?.()))) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_events"?.valueOf?.()))) ? "#d92314" : "transparent"), ["cursor"] : "pointer", ["width"] : "100%" }),onClick:on_click_84b72b6a8e0b8388ef06f5a059622e2f},jsx(Text_28a0453ca2a9db0c577594bf99b6efeb,{},))
  )
}


function Text_662bf248cfec0fe8ef76e8a7a143f246 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : (((((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_evidence_list"?.valueOf?.()) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_score"?.valueOf?.()))) || (true && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_evidence"?.valueOf?.()))) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_events"?.valueOf?.()))) ? "white" : "#4b5563"), ["fontSize"] : "13px", ["fontWeight"] : (((((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_evidence_list"?.valueOf?.()) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_score"?.valueOf?.()))) || (true && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_evidence"?.valueOf?.()))) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_events"?.valueOf?.()))) ? "700" : "500"), ["lineHeight"] : "1.45" })},"Duy\u1ec7t minh ch\u1ee9ng")
  )
}


function Box_0436ee8a034ebc8d8a6cec8afe6b9483 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_2212129137b6de300f9b605483b060a3 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.select_tab", ({ ["tab"] : "students_evidence_list" }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesBox,{css:({ ["padding"] : "8px 12px 8px 28px", ["borderRadius"] : "8px", ["background"] : (((((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_evidence_list"?.valueOf?.()) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_score"?.valueOf?.()))) || (true && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_evidence"?.valueOf?.()))) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_events"?.valueOf?.()))) ? "#d92314" : "transparent"), ["cursor"] : "pointer", ["width"] : "100%" }),onClick:on_click_2212129137b6de300f9b605483b060a3},jsx(Text_662bf248cfec0fe8ef76e8a7a143f246,{},))
  )
}


function Text_5d6e89fac7648e10ca433e8bf81cd4be () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : (((((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_events_list"?.valueOf?.()) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_score"?.valueOf?.()))) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_evidence"?.valueOf?.()))) || (true && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_events"?.valueOf?.()))) ? "white" : "#4b5563"), ["fontSize"] : "13px", ["fontWeight"] : (((((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_events_list"?.valueOf?.()) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_score"?.valueOf?.()))) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_evidence"?.valueOf?.()))) || (true && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_events"?.valueOf?.()))) ? "700" : "500"), ["lineHeight"] : "1.45" })},"Duy\u1ec7t s\u1ef1 ki\u1ec7n")
  )
}


function Box_2d6f2eedee7f77dcee5fd6e5ac5f9cbb () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_fea487324007d7310f537078af006456 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.select_tab", ({ ["tab"] : "students_events_list" }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesBox,{css:({ ["padding"] : "8px 12px 8px 28px", ["borderRadius"] : "8px", ["background"] : (((((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_events_list"?.valueOf?.()) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_score"?.valueOf?.()))) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_evidence"?.valueOf?.()))) || (true && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_events"?.valueOf?.()))) ? "#d92314" : "transparent"), ["cursor"] : "pointer", ["width"] : "100%" }),onClick:on_click_fea487324007d7310f537078af006456},jsx(Text_5d6e89fac7648e10ca433e8bf81cd4be,{},))
  )
}


function Text_15ec5f9fc9d846f92cec6e1e4ed05782 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : ((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_score"?.valueOf?.()) ? "white" : "#6b7280"), ["fontWeight"] : ((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_score"?.valueOf?.()) ? "700" : "500"), ["fontSize"] : "13px", ["lineHeight"] : "1.45" })},"Phi\u1ebfu \u0111i\u1ec3m r\u00e8n luy\u1ec7n")
  )
}


function Box_42ba5be87974fcf6d5e32ec81d99c667 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesBox,{css:({ ["padding"] : "8px 12px 8px 28px", ["borderRadius"] : "8px", ["background"] : ((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_score"?.valueOf?.()) ? "#d92314" : "transparent"), ["cursor"] : "default", ["width"] : "100%" })},jsx(Text_15ec5f9fc9d846f92cec6e1e4ed05782,{},))
  )
}


function Fragment_6072a0b8ab8ff21c191d721335731806 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.show_students_score_tab_rx_state_?(jsx(Fragment,{},jsx(Box_42ba5be87974fcf6d5e32ec81d99c667,{},))):(jsx(Fragment,{},))))
  )
}


function Text_2c726cf8f608fbba97c73e7430d53bf9 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : (((((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_evidence"?.valueOf?.()) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_score"?.valueOf?.()))) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_evidence"?.valueOf?.()))) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_events"?.valueOf?.()))) ? "white" : "#4b5563"), ["fontSize"] : "13px", ["fontWeight"] : (((((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_evidence"?.valueOf?.()) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_score"?.valueOf?.()))) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_evidence"?.valueOf?.()))) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_events"?.valueOf?.()))) ? "700" : "500"), ["lineHeight"] : "1.45" })},"Duy\u1ec7t minh ch\u1ee9ng")
  )
}


function Box_64a9e8ec52cba556961a42d3d2b321f6 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_abd512604dc46468e9bd93ed43325a05 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.select_tab", ({ ["tab"] : "students_evidence" }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesBox,{css:({ ["padding"] : "8px 12px 8px 28px", ["borderRadius"] : "8px", ["background"] : (((((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_evidence"?.valueOf?.()) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_score"?.valueOf?.()))) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_evidence"?.valueOf?.()))) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_events"?.valueOf?.()))) ? "#d92314" : "transparent"), ["cursor"] : "pointer", ["width"] : "100%" }),onClick:on_click_abd512604dc46468e9bd93ed43325a05},jsx(Text_2c726cf8f608fbba97c73e7430d53bf9,{},))
  )
}


function Fragment_55dbb822be9acbae1a6b237af08c592c () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.show_students_evidence_tab_rx_state_?(jsx(Fragment,{},jsx(Box_64a9e8ec52cba556961a42d3d2b321f6,{},))):(jsx(Fragment,{},))))
  )
}


function Text_ca3720ce1b6465f3669b785636e497c2 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : (((((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_events"?.valueOf?.()) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_score"?.valueOf?.()))) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_evidence"?.valueOf?.()))) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_events"?.valueOf?.()))) ? "white" : "#4b5563"), ["fontSize"] : "13px", ["fontWeight"] : (((((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_events"?.valueOf?.()) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_score"?.valueOf?.()))) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_evidence"?.valueOf?.()))) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_events"?.valueOf?.()))) ? "700" : "500"), ["lineHeight"] : "1.45" })},"Duy\u1ec7t s\u1ef1 ki\u1ec7n")
  )
}


function Box_6928a1b2d19c212c63ea61074c7cdb6f () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_81f6d815dac2b7b49653372f5bfd34a4 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.select_tab", ({ ["tab"] : "students_events" }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesBox,{css:({ ["padding"] : "8px 12px 8px 28px", ["borderRadius"] : "8px", ["background"] : (((((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_events"?.valueOf?.()) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_score"?.valueOf?.()))) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_evidence"?.valueOf?.()))) || (false && (reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_events"?.valueOf?.()))) ? "#d92314" : "transparent"), ["cursor"] : "pointer", ["width"] : "100%" }),onClick:on_click_81f6d815dac2b7b49653372f5bfd34a4},jsx(Text_ca3720ce1b6465f3669b785636e497c2,{},))
  )
}


function Fragment_a7ac28ac76993d1afec9028b1caacf0a () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.show_students_events_tab_rx_state_?(jsx(Fragment,{},jsx(Box_6928a1b2d19c212c63ea61074c7cdb6f,{},))):(jsx(Fragment,{},))))
  )
}


function Fragment_f92a4b4efbe234898f67dce798e12029 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},((reflex___state____state__ptit_reflex___state____conduct_state.current_user_role_rx_state_?.valueOf?.() === "class_monitor"?.valueOf?.())?(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%", ["paddingBottom"] : "4px" }),direction:"column",gap:"2"},jsx(Box_d8863f0d003c7d4672865f4f883831d1,{},),jsx(Box_0436ee8a034ebc8d8a6cec8afe6b9483,{},),jsx(Box_2d6f2eedee7f77dcee5fd6e5ac5f9cbb,{},)))):(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%", ["paddingBottom"] : "4px" }),direction:"column",gap:"2"},jsx(Fragment_6072a0b8ab8ff21c191d721335731806,{},),jsx(Fragment_55dbb822be9acbae1a6b237af08c592c,{},),jsx(Fragment_a7ac28ac76993d1afec9028b1caacf0a,{},))))))
  )
}


function Fragment_96765424e79a23794f1959f0d228a685 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.nav_students_open_rx_state_?(jsx(Fragment_f92a4b4efbe234898f67dce798e12029,{},)):(jsx(Fragment,{},))))
  )
}


function Fragment_71b912e99d42d66054c6d1a1aee2d68d () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.show_student_directory_tab_rx_state_?(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"2"},jsx(Flex_687716799a134450add4d34227032395,{},),jsx(Fragment_96765424e79a23794f1959f0d228a685,{},)))):(jsx(Fragment,{},))))
  )
}


function Text_c352401e51fa391995bf349a7b66f403 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : ((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "evidence"?.valueOf?.()) ? "white" : "#374151"), ["fontSize"] : "14px", ["fontWeight"] : ((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "evidence"?.valueOf?.()) ? "700" : "500"), ["lineHeight"] : "1.45" })},"Khai b\u00e1o minh ch\u1ee9ng")
  )
}


function Box_2e3ac0a1940803bcc9eb49ec1767cb00 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_b84e82990ddd446354116a08941bb8a7 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.select_tab", ({ ["tab"] : "evidence" }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesBox,{css:({ ["padding"] : "12px 14px", ["borderRadius"] : "8px", ["background"] : ((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "evidence"?.valueOf?.()) ? "#d92314" : "transparent"), ["cursor"] : "pointer", ["width"] : "100%" }),onClick:on_click_b84e82990ddd446354116a08941bb8a7},jsx(Text_c352401e51fa391995bf349a7b66f403,{},))
  )
}


function Text_fdda790bfeb0e53b2bcfe3c187918871 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : ((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "events"?.valueOf?.()) ? "white" : "#374151"), ["fontSize"] : "14px", ["fontWeight"] : ((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "events"?.valueOf?.()) ? "700" : "500"), ["lineHeight"] : "1.45" })},"S\u1ef1 ki\u1ec7n \u0111\u00e3 tham gia")
  )
}


function Box_ae499f7ea18c491af4df1a3ba4c8cbe3 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_533c8f170686b45afec760b40d8fa004 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.select_tab", ({ ["tab"] : "events" }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesBox,{css:({ ["padding"] : "12px 14px", ["borderRadius"] : "8px", ["background"] : ((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "events"?.valueOf?.()) ? "#d92314" : "transparent"), ["cursor"] : "pointer", ["width"] : "100%" }),onClick:on_click_533c8f170686b45afec760b40d8fa004},jsx(Text_fdda790bfeb0e53b2bcfe3c187918871,{},))
  )
}


function Fragment_cffa8700d781549bc73290504d7ec33e () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.show_declaration_tabs_rx_state_?(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"2"},jsx(Box_2e3ac0a1940803bcc9eb49ec1767cb00,{},),jsx(Box_ae499f7ea18c491af4df1a3ba4c8cbe3,{},)))):(jsx(Fragment,{},))))
  )
}


function Text_f42d558e99264f728283dbcdf7973955 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : ((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "admin_events"?.valueOf?.()) ? "white" : "#374151"), ["fontSize"] : "14px", ["fontWeight"] : ((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "admin_events"?.valueOf?.()) ? "700" : "500"), ["lineHeight"] : "1.45" })},"T\u1ea1o s\u1ef1 ki\u1ec7n")
  )
}


function Box_9ef8bab084bbec1ce51d0d897fd2fe02 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_ab8ea0851e8b0fad384aeca7b7e85371 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.select_tab", ({ ["tab"] : "admin_events" }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesBox,{css:({ ["padding"] : "12px 14px", ["borderRadius"] : "8px", ["background"] : ((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "admin_events"?.valueOf?.()) ? "#d92314" : "transparent"), ["cursor"] : "pointer", ["width"] : "100%" }),onClick:on_click_ab8ea0851e8b0fad384aeca7b7e85371},jsx(Text_f42d558e99264f728283dbcdf7973955,{},))
  )
}


function Fragment_a6867a429b5de75797a70aefcd2241f2 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},((reflex___state____state__ptit_reflex___state____conduct_state.current_user_role_rx_state_?.valueOf?.() === "admin"?.valueOf?.())?(jsx(Fragment,{},jsx(Box_9ef8bab084bbec1ce51d0d897fd2fe02,{},))):(jsx(Fragment,{},))))
  )
}


function Text_3f987df903b3377ab8f80eab019865a7 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : ((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "score"?.valueOf?.()) ? "white" : "#374151"), ["fontSize"] : "14px", ["fontWeight"] : ((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "score"?.valueOf?.()) ? "700" : "500"), ["lineHeight"] : "1.45" })},"Phi\u1ebfu \u0111i\u1ec3m r\u00e8n luy\u1ec7n")
  )
}


function Box_b4dacc33fa8dbdf5c6a523b666de094b () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_9f6eed25febb14ebb075d934b5b5a6c0 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.select_tab", ({ ["tab"] : "score" }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesBox,{css:({ ["padding"] : "12px 14px", ["borderRadius"] : "8px", ["background"] : ((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "score"?.valueOf?.()) ? "#d92314" : "transparent"), ["cursor"] : "pointer", ["width"] : "100%" }),onClick:on_click_9f6eed25febb14ebb075d934b5b5a6c0},jsx(Text_3f987df903b3377ab8f80eab019865a7,{},))
  )
}


function Fragment_6a6c3ffcb4691f5d3d68a25a0c1dce26 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.show_self_score_tab_rx_state_?(jsx(Fragment,{},jsx(Box_b4dacc33fa8dbdf5c6a523b666de094b,{},))):(jsx(Fragment,{},))))
  )
}


function Text_dc60127fbd1196d0096095281235a7d7 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["fontWeight"] : "600", ["color"] : ((reflex___state____state__ptit_reflex___state____conduct_state.flash_kind_rx_state_?.valueOf?.() === "error"?.valueOf?.()) ? "#b91c1c" : ((reflex___state____state__ptit_reflex___state____conduct_state.flash_kind_rx_state_?.valueOf?.() === "success"?.valueOf?.()) ? "#166534" : "#075985")) })},reflex___state____state__ptit_reflex___state____conduct_state.flash_message_rx_state_)
  )
}


function Text_51818710a4a8900f2d7fb2ee7ea923bf () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_8a53c7f27cc818ff20f0474c0ec04cc1 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.clear_flash", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : ((reflex___state____state__ptit_reflex___state____conduct_state.flash_kind_rx_state_?.valueOf?.() === "error"?.valueOf?.()) ? "#b91c1c" : ((reflex___state____state__ptit_reflex___state____conduct_state.flash_kind_rx_state_?.valueOf?.() === "success"?.valueOf?.()) ? "#166534" : "#075985")), ["fontSize"] : "13px", ["cursor"] : "pointer" }),onClick:on_click_8a53c7f27cc818ff20f0474c0ec04cc1},"\u0110\u00f3ng")
  )
}


function Flex_19b8b913115ba30ed98439748318cd6e () {
  
                useEffect(() => {
                    ((...args) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.schedule_flash_auto_clear", ({  }), ({  })))], args, ({  }))))()
                    return () => {
                        
                    }
                }, []);
const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["padding"] : "12px 16px", ["background"] : ((reflex___state____state__ptit_reflex___state____conduct_state.flash_kind_rx_state_?.valueOf?.() === "error"?.valueOf?.()) ? "#fee2e2" : ((reflex___state____state__ptit_reflex___state____conduct_state.flash_kind_rx_state_?.valueOf?.() === "success"?.valueOf?.()) ? "#dcfce7" : "#e0f2fe")), ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "10px" }),direction:"row",justify:"between",key:reflex___state____state__ptit_reflex___state____conduct_state.flash_token_rx_state_,gap:"3"},jsx(Text_dc60127fbd1196d0096095281235a7d7,{},),jsx(Text_51818710a4a8900f2d7fb2ee7ea923bf,{},))
  )
}


function Fragment_ace4f9daeb0704d294dde9e1d0d362fd () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(!((reflex___state____state__ptit_reflex___state____conduct_state.flash_message_rx_state_?.valueOf?.() === ""?.valueOf?.()))?(jsx(Fragment,{},jsx(Flex_19b8b913115ba30ed98439748318cd6e,{},))):(jsx(Fragment,{},))))
  )
}


function Text_96b3be038167bbef2f158960e935b360 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["color"] : "#6b7280" })},reflex___state____state__ptit_reflex___state____conduct_state.student_profile_rx_state_?.["full_name"])
  )
}


function Text_b86e7485bb566a63176ae6bb0b014910 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["fontWeight"] : "700", ["color"] : "white" })},reflex___state____state__ptit_reflex___state____conduct_state.student_profile_rx_state_?.["class_name"])
  )
}


function Text_21eef9ba12f7461dd1c80fbf293ea4ef () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["fontWeight"] : "700", ["color"] : "#1d4ed8" })},reflex___state____state__ptit_reflex___state____conduct_state.student_profile_rx_state_?.["gpa"])
  )
}


function Button_f1f2c0d7c048b6042ea24909e6ceb353 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_c2c4730087e99ad12bb148f04184e1c0 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.cancel_profile_edit", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : "white", ["color"] : "#1f2937", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:on_click_c2c4730087e99ad12bb148f04184e1c0},"H\u1ee7y")
  )
}


function Button_994fa3f851ee377b721b4dc83abfa02b () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_5ffe3de04e51331107f36e4f21942a62 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.save_profile", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : "#d92314", ["color"] : "white", ["border"] : "none", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:on_click_5ffe3de04e51331107f36e4f21942a62},"L\u01b0u th\u00f4ng tin")
  )
}


function Button_a0cae056386f22e6b0b429f3f9ed11f4 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_51d16225615e7a699920d26490e861af = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.start_profile_edit", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : "white", ["color"] : "#1f2937", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:on_click_51d16225615e7a699920d26490e861af},"S\u1eeda th\u00f4ng tin")
  )
}


function Fragment_b7702102a574ad3082c81afa3df334b0 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.profile_editing_rx_state_?(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["flexWrap"] : "wrap" }),direction:"row",gap:"2"},jsx(Button_f1f2c0d7c048b6042ea24909e6ceb353,{},),jsx(Button_994fa3f851ee377b721b4dc83abfa02b,{},)))):(jsx(Fragment,{},jsx(Button_a0cae056386f22e6b0b429f3f9ed11f4,{},)))))
  )
}


function Fragment_addf2e5aa013d747bade4bcf5945e670 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.can_edit_own_profile_rx_state_?(jsx(Fragment_b7702102a574ad3082c81afa3df334b0,{},)):(jsx(Fragment,{},))))
  )
}


function Debounceinput_9dbccc016e23f0a44c414a8238fe2834 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_cebc6d3df063a9c8ff6656778781bc45 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_profile_field", ({ ["field_name"] : "profile_edit_full_name", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_cebc6d3df063a9c8ff6656778781bc45,placeholder:"Nh\u1eadp h\u1ecd t\u00ean",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.profile_edit_full_name_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.profile_edit_full_name_rx_state_ : "")},)
  )
}


function Debounceinput_87cea222cd1d2ae8f36d2a23987f6651 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_3a53680a487e0cf09688f54714b125c1 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_profile_field", ({ ["field_name"] : "profile_edit_email", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_3a53680a487e0cf09688f54714b125c1,placeholder:"Nh\u1eadp email",type:"email",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.profile_edit_email_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.profile_edit_email_rx_state_ : "")},)
  )
}


function Debounceinput_a50f3de087caead8e5538ebcd8773569 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_d1076ef20933e4f6a553c4fa99919716 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_profile_field", ({ ["field_name"] : "profile_edit_phone", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_d1076ef20933e4f6a553c4fa99919716,placeholder:"Nh\u1eadp s\u1ed1 \u0111i\u1ec7n tho\u1ea1i",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.profile_edit_phone_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.profile_edit_phone_rx_state_ : "")},)
  )
}


function Debounceinput_a7d8f1cdedef268a599e001530211acd () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_d55ccd013e2a16ba48fb499785c4acce = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_profile_field", ({ ["field_name"] : "profile_edit_birth_date", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_d55ccd013e2a16ba48fb499785c4acce,placeholder:"Ch\u1ecdn ng\u00e0y sinh",type:"date",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.profile_edit_birth_date_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.profile_edit_birth_date_rx_state_ : "")},)
  )
}


function Select__group_927e24009c346bf8c1ef212131b2d2db () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesSelect.Group,{},"",Array.prototype.map.call(reflex___state____state__ptit_reflex___state____conduct_state.register_gender_options_rx_state_ ?? [],((item_rx_state_,index_d6d6157c99650830f12a866606ea87b7)=>(jsx(RadixThemesSelect.Item,{key:index_d6d6157c99650830f12a866606ea87b7,value:item_rx_state_},item_rx_state_)))))
  )
}


function Select__root_434de5cd7713b5108e1bc43405e8f472 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_fe134545354f888597b9cf1d5dbf3dbb = useCallback(((_ev_0) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_profile_field", ({ ["field_name"] : "profile_edit_gender", ["value"] : _ev_0 }), ({  })))], [_ev_0], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesSelect.Root,{css:({ ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white", ["color"] : "#1f2937" }),onValueChange:on_change_fe134545354f888597b9cf1d5dbf3dbb,value:reflex___state____state__ptit_reflex___state____conduct_state.profile_edit_gender_rx_state_},jsx(RadixThemesSelect.Trigger,{css:({ ["width"] : "100%" })},),jsx(RadixThemesSelect.Content,{},jsx(Select__group_927e24009c346bf8c1ef212131b2d2db,{},)))
  )
}


function Text_367fec763afd24a1abd8ab755df64cb4 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["color"] : "#1f2937", ["fontWeight"] : "600", ["lineHeight"] : "1.5" })},reflex___state____state__ptit_reflex___state____conduct_state.student_profile_rx_state_?.["student_code"])
  )
}


function Text_54e01f8067739fdc3e05513e431519a3 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["color"] : "#1f2937", ["fontWeight"] : "600", ["lineHeight"] : "1.5" })},reflex___state____state__ptit_reflex___state____conduct_state.student_profile_rx_state_?.["class_name"])
  )
}


function Text_c39bec6107333df282e924e5817e8e17 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["color"] : "#1f2937", ["fontWeight"] : "600", ["lineHeight"] : "1.5" })},reflex___state____state__ptit_reflex___state____conduct_state.student_profile_rx_state_?.["faculty"])
  )
}


function Text_5cacf048b02a9cdc556007fd5b58a6e3 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["color"] : "#1f2937", ["fontWeight"] : "600", ["lineHeight"] : "1.5" })},reflex___state____state__ptit_reflex___state____conduct_state.student_profile_rx_state_?.["major"])
  )
}


function Text_b6c8fb08f1c2b4c10ddb651e33263248 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["color"] : "#1f2937", ["fontWeight"] : "600", ["lineHeight"] : "1.5" })},reflex___state____state__ptit_reflex___state____conduct_state.student_profile_rx_state_?.["advisor_name"])
  )
}


function Text_e9450c093b02eeaff61ffc7bac2cdbc6 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["color"] : "#1f2937", ["fontWeight"] : "600", ["lineHeight"] : "1.5" })},reflex___state____state__ptit_reflex___state____conduct_state.student_profile_rx_state_?.["class_monitor_name"])
  )
}


function Text_5a64e70a2150007b892f9ffd4daabff5 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["color"] : "#1f2937", ["fontWeight"] : "600", ["lineHeight"] : "1.5" })},reflex___state____state__ptit_reflex___state____conduct_state.student_profile_rx_state_?.["status"])
  )
}


function Debounceinput_f38b1497721f75a03b575d8c7a3a126e () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_ad50b5e17b43f2fdd4aad90ffbfd3db5 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_profile_field", ({ ["field_name"] : "profile_edit_address", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["minHeight"] : "100px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextArea,onChange:on_change_ad50b5e17b43f2fdd4aad90ffbfd3db5,placeholder:"Nh\u1eadp \u0111\u1ecba ch\u1ec9 hi\u1ec7n t\u1ea1i",value:reflex___state____state__ptit_reflex___state____conduct_state.profile_edit_address_rx_state_},)
  )
}


function Text_8b22390aea076f07aaec097c0f2f0018 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["color"] : "#1f2937", ["fontWeight"] : "600", ["lineHeight"] : "1.5" })},reflex___state____state__ptit_reflex___state____conduct_state.student_profile_rx_state_?.["full_name"])
  )
}


function Text_f8d985316ea164f5d2ac23e77b81f02c () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["color"] : "#1f2937", ["fontWeight"] : "600", ["lineHeight"] : "1.5" })},reflex___state____state__ptit_reflex___state____conduct_state.student_profile_rx_state_?.["email"])
  )
}


function Text_932e2b30715fc0294611bd5c2713bd37 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["color"] : "#1f2937", ["fontWeight"] : "600", ["lineHeight"] : "1.5" })},reflex___state____state__ptit_reflex___state____conduct_state.student_profile_rx_state_?.["phone"])
  )
}


function Text_8aeb12cdb3d926cdea1b028b0cd4df99 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["color"] : "#1f2937", ["fontWeight"] : "600", ["lineHeight"] : "1.5" })},reflex___state____state__ptit_reflex___state____conduct_state.student_profile_rx_state_?.["birth_date"])
  )
}


function Text_718883db4e6d0d41fcb5ef0fa77b5e1e () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["color"] : "#1f2937", ["fontWeight"] : "600", ["lineHeight"] : "1.5" })},reflex___state____state__ptit_reflex___state____conduct_state.student_profile_rx_state_?.["gender"])
  )
}


function Text_31b44af430251a8d013b4e30f2091c46 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["color"] : "#374151", ["lineHeight"] : "1.7" })},reflex___state____state__ptit_reflex___state____conduct_state.student_profile_rx_state_?.["address"])
  )
}


function Select__group_91fe2be0f0af2134f6d6b2335837614e () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesSelect.Group,{},"",Array.prototype.map.call(reflex___state____state__ptit_reflex___state____conduct_state.semester_names_rx_state_ ?? [],((item_rx_state_,index_d6d6157c99650830f12a866606ea87b7)=>(jsx(RadixThemesSelect.Item,{key:index_d6d6157c99650830f12a866606ea87b7,value:item_rx_state_},item_rx_state_)))))
  )
}


function Select__root_ee6018cea39361f01aceb82959ee1920 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_fc43cac6d9a225b19126d3c9e8dbcee6 = useCallback(((_ev_0) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.select_semester_by_name", ({ ["name"] : _ev_0 }), ({  })))], [_ev_0], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesSelect.Root,{css:({ ["minWidth"] : "240px", ["maxWidth"] : "280px", ["height"] : "40px", ["border"] : "1px solid #d92314", ["borderRadius"] : "10px", ["background"] : "white", ["color"] : "#1f2937", ["fontSize"] : "14px", ["fontWeight"] : "500", ["paddingLeft"] : "12px", ["paddingRight"] : "12px" }),onValueChange:on_change_fc43cac6d9a225b19126d3c9e8dbcee6,value:reflex___state____state__ptit_reflex___state____conduct_state.selected_semester_name_rx_state_},jsx(RadixThemesSelect.Trigger,{css:({ ["width"] : "280px", ["flexShrink"] : "0" })},),jsx(RadixThemesSelect.Content,{},jsx(Select__group_91fe2be0f0af2134f6d6b2335837614e,{},)))
  )
}


function Debounceinput_1ed7b940d15d2d825e00ced40c95e4c8 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_a5086fc3a5c8ecb0e58010b9215541c3 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_advisor_gpa_input", ({ ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_a5086fc3a5c8ecb0e58010b9215541c3,placeholder:"V\u00ed d\u1ee5: 3.25",type:"number",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.advisor_gpa_input_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.advisor_gpa_input_rx_state_ : "")},)
  )
}


function Button_a7091b7cb6b7f860a7f5ee21b702afb6 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_572e0ddfd15d50b5283a2e5debf85e55 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.save_advisor_gpa", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : "#d92314", ["color"] : "white", ["border"] : "none", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:on_click_572e0ddfd15d50b5283a2e5debf85e55},"L\u01b0u GPA")
  )
}


function Fragment_55110f80088d2bcc9dcd823a3fdcd630 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.can_edit_student_gpa_rx_state_?(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "16px", ["background"] : "#fffbeb", ["border"] : "1px solid #fde68a", ["borderRadius"] : "12px" })},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"3"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%", ["flexWrap"] : "wrap" }),direction:"row",justify:"between",gap:"3"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["fontWeight"] : "800", ["color"] : "#1f2937" })},"GPA h\u1ecdc k\u1ef3"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["lineHeight"] : "1.6" })},"C\u1ed1 v\u1ea5n nh\u1eadp GPA t\u1ea1i \u0111\u00e2y \u0111\u1ec3 h\u1ec7 th\u1ed1ng t\u1ef1 t\u00ednh ti\u00eau ch\u00ed k\u1ebft qu\u1ea3 h\u1ecdc t\u1eadp trong phi\u1ebfu r\u00e8n luy\u1ec7n.")),jsx(Select__root_ee6018cea39361f01aceb82959ee1920,{},)),jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["flexWrap"] : "wrap" }),direction:"row",gap:"3"},jsx(RadixThemesBox,{css:({ ["width"] : "240px", ["maxWidth"] : "100%" })},jsx(Debounceinput_1ed7b940d15d2d825e00ced40c95e4c8,{},)),jsx(Button_a7091b7cb6b7f860a7f5ee21b702afb6,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280" })},"Thang 4.0")))))):(jsx(Fragment,{},))))
  )
}


function Fragment_6f92db0302bda406d8f5eafb59d1375b () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.can_edit_own_profile_rx_state_?(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"4"},jsx(RadixThemesGrid,{columns:"3",css:({ ["width"] : "100%" }),gap:"5"},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"H\u1ecd t\u00ean"),jsx(Debounceinput_9dbccc016e23f0a44c414a8238fe2834,{},)),jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"Email"),jsx(Debounceinput_87cea222cd1d2ae8f36d2a23987f6651,{},)),jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i"),jsx(Debounceinput_a50f3de087caead8e5538ebcd8773569,{},)),jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"Ng\u00e0y sinh"),jsx(Debounceinput_a7d8f1cdedef268a599e001530211acd,{},)),jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"Gi\u1edbi t\u00ednh"),jsx(Select__root_434de5cd7713b5108e1bc43405e8f472,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"M\u00e3 sinh vi\u00ean"),jsx(Text_367fec763afd24a1abd8ab755df64cb4,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"L\u1edbp"),jsx(Text_54e01f8067739fdc3e05513e431519a3,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"Khoa"),jsx(Text_c39bec6107333df282e924e5817e8e17,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"Ng\u00e0nh"),jsx(Text_5cacf048b02a9cdc556007fd5b58a6e3,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"Th\u00f4ng tin gi\u1ea3ng vi\u00ean"),jsx(Text_b6c8fb08f1c2b4c10ddb651e33263248,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"Ban c\u00e1n s\u1ef1"),jsx(Text_e9450c093b02eeaff61ffc7bac2cdbc6,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"Tr\u1ea1ng th\u00e1i"),jsx(Text_5a64e70a2150007b892f9ffd4daabff5,{},))),jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"\u0110\u1ecba ch\u1ec9"),jsx(Debounceinput_f38b1497721f75a03b575d8c7a3a126e,{},))))):(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"4"},jsx(RadixThemesGrid,{columns:"3",css:({ ["width"] : "100%" }),gap:"5"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"M\u00e3 sinh vi\u00ean"),jsx(Text_367fec763afd24a1abd8ab755df64cb4,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"H\u1ecd t\u00ean"),jsx(Text_8b22390aea076f07aaec097c0f2f0018,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"L\u1edbp"),jsx(Text_54e01f8067739fdc3e05513e431519a3,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"Khoa"),jsx(Text_c39bec6107333df282e924e5817e8e17,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"Ng\u00e0nh"),jsx(Text_5cacf048b02a9cdc556007fd5b58a6e3,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"Th\u00f4ng tin gi\u1ea3ng vi\u00ean"),jsx(Text_b6c8fb08f1c2b4c10ddb651e33263248,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"Ban c\u00e1n s\u1ef1"),jsx(Text_e9450c093b02eeaff61ffc7bac2cdbc6,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"Email"),jsx(Text_f8d985316ea164f5d2ac23e77b81f02c,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i"),jsx(Text_932e2b30715fc0294611bd5c2713bd37,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"Ng\u00e0y sinh"),jsx(Text_8aeb12cdb3d926cdea1b028b0cd4df99,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"Gi\u1edbi t\u00ednh"),jsx(Text_718883db4e6d0d41fcb5ef0fa77b5e1e,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"Tr\u1ea1ng th\u00e1i"),jsx(Text_5a64e70a2150007b892f9ffd4daabff5,{},))),jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"\u0110\u1ecba ch\u1ec9"),jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "14px 16px", ["background"] : "#f8fafc", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "10px" })},jsx(Text_31b44af430251a8d013b4e30f2091c46,{},))),jsx(Fragment_55110f80088d2bcc9dcd823a3fdcd630,{},))))))
  )
}


function Fragment_05c38e8e5e2e41ba82b6285f7031b5c2 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.profile_editing_rx_state_?(jsx(Fragment_6f92db0302bda406d8f5eafb59d1375b,{},)):(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"4"},jsx(RadixThemesGrid,{columns:"3",css:({ ["width"] : "100%" }),gap:"5"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"M\u00e3 sinh vi\u00ean"),jsx(Text_367fec763afd24a1abd8ab755df64cb4,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"H\u1ecd t\u00ean"),jsx(Text_8b22390aea076f07aaec097c0f2f0018,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"L\u1edbp"),jsx(Text_54e01f8067739fdc3e05513e431519a3,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"Khoa"),jsx(Text_c39bec6107333df282e924e5817e8e17,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"Ng\u00e0nh"),jsx(Text_5cacf048b02a9cdc556007fd5b58a6e3,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"Th\u00f4ng tin gi\u1ea3ng vi\u00ean"),jsx(Text_b6c8fb08f1c2b4c10ddb651e33263248,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"Ban c\u00e1n s\u1ef1"),jsx(Text_e9450c093b02eeaff61ffc7bac2cdbc6,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"Email"),jsx(Text_f8d985316ea164f5d2ac23e77b81f02c,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i"),jsx(Text_932e2b30715fc0294611bd5c2713bd37,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"Ng\u00e0y sinh"),jsx(Text_8aeb12cdb3d926cdea1b028b0cd4df99,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"Gi\u1edbi t\u00ednh"),jsx(Text_718883db4e6d0d41fcb5ef0fa77b5e1e,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"Tr\u1ea1ng th\u00e1i"),jsx(Text_5a64e70a2150007b892f9ffd4daabff5,{},))),jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"\u0110\u1ecba ch\u1ec9"),jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "14px 16px", ["background"] : "#f8fafc", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "10px" })},jsx(Text_31b44af430251a8d013b4e30f2091c46,{},))),jsx(Fragment_55110f80088d2bcc9dcd823a3fdcd630,{},))))))
  )
}


function Text_db80af55de392cd4435d181999a003d2 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["color"] : "#6b7280" })},reflex___state____state__ptit_reflex___state____conduct_state.current_user_name_rx_state_)
  )
}


function Text_01153135d78c0992ed3983f591b3c683 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["color"] : "#1f2937", ["fontWeight"] : "600", ["lineHeight"] : "1.5" })},reflex___state____state__ptit_reflex___state____conduct_state.current_user_name_rx_state_)
  )
}


function Text_f45a435a5367d745d099bef13d6c296b () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["color"] : "#1f2937", ["fontWeight"] : "600", ["lineHeight"] : "1.5" })},reflex___state____state__ptit_reflex___state____conduct_state.current_user_email_rx_state_)
  )
}


function Text_5f8842da68610e0cb26d894faecf6526 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["color"] : "#1f2937", ["fontWeight"] : "600", ["lineHeight"] : "1.5" })},reflex___state____state__ptit_reflex___state____conduct_state.current_user_faculty_rx_state_)
  )
}


function Text_45a3c183f143d3908fe9f1da1d25c43c () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["color"] : "#1f2937", ["fontWeight"] : "600", ["lineHeight"] : "1.5" })},reflex___state____state__ptit_reflex___state____conduct_state.current_user_role_label_rx_state_)
  )
}


function Text_58a019ad6e1ce292f1f79f65d34161d6 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["color"] : "#1f2937", ["fontWeight"] : "600", ["lineHeight"] : "1.5" })},reflex___state____state__ptit_reflex___state____conduct_state.current_user_class_name_rx_state_)
  )
}


function Fragment_0a1ee05954bf15e97be277784662c0a0 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},((reflex___state____state__ptit_reflex___state____conduct_state.current_user_role_rx_state_?.valueOf?.() === "advisor"?.valueOf?.())?(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "20px", ["background"] : "white", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "12px" })},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"4"},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["flexWrap"] : "wrap" }),direction:"row",justify:"between",gap:"3"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"column",gap:"0"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "18px", ["fontWeight"] : "800", ["color"] : "#1f2937" })},"Th\u00f4ng tin gi\u1ea3ng vi\u00ean"),jsx(Text_db80af55de392cd4435d181999a003d2,{},)),jsx(RadixThemesBox,{css:({ ["padding"] : "6px 12px", ["borderRadius"] : "999px", ["background"] : "#111827" })},jsx(Text_2351b54af388b792761e6d24fb6636ed,{},))),jsx(RadixThemesGrid,{columns:"2",css:({ ["width"] : "100%" }),gap:"5"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"H\u1ecd t\u00ean"),jsx(Text_01153135d78c0992ed3983f591b3c683,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"Email"),jsx(Text_f45a435a5367d745d099bef13d6c296b,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"\u0110\u01a1n v\u1ecb"),jsx(Text_5f8842da68610e0cb26d894faecf6526,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"L\u1edbp ph\u1ee5 tr\u00e1ch"),jsx(Text_58a019ad6e1ce292f1f79f65d34161d6,{},))))))):(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "20px", ["background"] : "white", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "12px" })},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"4"},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["flexWrap"] : "wrap" }),direction:"row",justify:"between",gap:"3"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"column",gap:"0"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "18px", ["fontWeight"] : "800", ["color"] : "#1f2937" })},"Th\u00f4ng tin sinh vi\u00ean"),jsx(Text_96b3be038167bbef2f158960e935b360,{},)),jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["flexWrap"] : "wrap" }),direction:"row",gap:"2"},jsx(RadixThemesBox,{css:({ ["padding"] : "6px 12px", ["borderRadius"] : "999px", ["background"] : "#111827" })},jsx(Text_b86e7485bb566a63176ae6bb0b014910,{},)),jsx(RadixThemesBox,{css:({ ["background"] : "#eff6ff", ["borderRadius"] : "999px", ["padding"] : "6px 12px" })},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",direction:"row",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["fontWeight"] : "700", ["color"] : "#1d4ed8" })},"GPA"),jsx(Text_21eef9ba12f7461dd1c80fbf293ea4ef,{},))),jsx(Fragment_addf2e5aa013d747bade4bcf5945e670,{},))),jsx(Fragment_05c38e8e5e2e41ba82b6285f7031b5c2,{},)))))))
  )
}


function Fragment_978350fce2caa949f7b54624b28189c7 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},((reflex___state____state__ptit_reflex___state____conduct_state.current_user_role_rx_state_?.valueOf?.() === "admin"?.valueOf?.())?(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "20px", ["background"] : "white", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "12px" })},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"4"},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["flexWrap"] : "wrap" }),direction:"row",justify:"between",gap:"3"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"column",gap:"0"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "18px", ["fontWeight"] : "800", ["color"] : "#1f2937" })},"Th\u00f4ng tin qu\u1ea3n tr\u1ecb vi\u00ean"),jsx(Text_db80af55de392cd4435d181999a003d2,{},)),jsx(RadixThemesBox,{css:({ ["padding"] : "6px 12px", ["borderRadius"] : "999px", ["background"] : "#111827" })},jsx(Text_2351b54af388b792761e6d24fb6636ed,{},))),jsx(RadixThemesGrid,{columns:"2",css:({ ["width"] : "100%" }),gap:"5"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"H\u1ecd t\u00ean"),jsx(Text_01153135d78c0992ed3983f591b3c683,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"Email"),jsx(Text_f45a435a5367d745d099bef13d6c296b,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"\u0110\u01a1n v\u1ecb"),jsx(Text_5f8842da68610e0cb26d894faecf6526,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "180px", ["width"] : "100%" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280", ["fontWeight"] : "700", ["textTransform"] : "uppercase" })},"Vai tr\u00f2"),jsx(Text_45a3c183f143d3908fe9f1da1d25c43c,{},))))))):(jsx(Fragment_0a1ee05954bf15e97be277784662c0a0,{},))))
  )
}


function Fragment_da2f1848627d3778054dbf89217d2e27 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "student_detail"?.valueOf?.())?(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "20px", ["background"] : "white", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "12px" })},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"4"},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["flexWrap"] : "wrap" }),direction:"row",justify:"between",gap:"3"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"column",gap:"0"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "18px", ["fontWeight"] : "800", ["color"] : "#1f2937" })},"Th\u00f4ng tin sinh vi\u00ean"),jsx(Text_96b3be038167bbef2f158960e935b360,{},)),jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["flexWrap"] : "wrap" }),direction:"row",gap:"2"},jsx(RadixThemesBox,{css:({ ["padding"] : "6px 12px", ["borderRadius"] : "999px", ["background"] : "#111827" })},jsx(Text_b86e7485bb566a63176ae6bb0b014910,{},)),jsx(RadixThemesBox,{css:({ ["background"] : "#eff6ff", ["borderRadius"] : "999px", ["padding"] : "6px 12px" })},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",direction:"row",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["fontWeight"] : "700", ["color"] : "#1d4ed8" })},"GPA"),jsx(Text_21eef9ba12f7461dd1c80fbf293ea4ef,{},))),jsx(Fragment_addf2e5aa013d747bade4bcf5945e670,{},))),jsx(Fragment_05c38e8e5e2e41ba82b6285f7031b5c2,{},))))):(jsx(Fragment_978350fce2caa949f7b54624b28189c7,{},))))
  )
}


function Fragment_265f21a195b0dc4dc19ed007f2fd2f39 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_evidence"?.valueOf?.())?(jsx(Fragment,{},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "22px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},"Duy\u1ec7t minh ch\u1ee9ng"))):(jsx(Fragment,{},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "22px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},"Khai b\u00e1o minh ch\u1ee9ng")))))
  )
}


function Text_2bd28a55762d5259eebfdc5f34f92221 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["fontWeight"] : "600", ["color"] : "#1e3a8a" })},reflex___state____state__ptit_reflex___state____conduct_state.grading_target_banner_text_rx_state_)
  )
}


function Fragment_4825087903813d4c4fdeb030523e3f8e () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(!((reflex___state____state__ptit_reflex___state____conduct_state.grading_target_banner_text_rx_state_?.valueOf?.() === ""?.valueOf?.()))?(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "10px 14px", ["background"] : "#eff6ff", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px" })},jsx(Text_2bd28a55762d5259eebfdc5f34f92221,{},)))):(jsx(Fragment,{},))))
  )
}


function Fragment_e481484b0e70c316b06b1f0a2afbbf4c () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_evidence"?.valueOf?.())?(jsx(Fragment,{},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "18px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},"Duy\u1ec7t minh ch\u1ee9ng"))):(jsx(Fragment,{},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "18px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},"Khai b\u00e1o minh ch\u1ee9ng")))))
  )
}


function Text_8e2de377a3aac2e9e3e7ac3f4b525aab () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["color"] : "#6b7280" })},reflex___state____state__ptit_reflex___state____conduct_state.selected_student_name_rx_state_)
  )
}


function Text_77e76f365172eccc54e58040eda12034 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["color"] : "#6b7280" })},reflex___state____state__ptit_reflex___state____conduct_state.selected_student_class_rx_state_)
  )
}


function Text_84db5c447968c18c7a5993ff3bc1a4f8 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["color"] : "#1d4ed8", ["fontWeight"] : "600" })},reflex___state____state__ptit_reflex___state____conduct_state.selected_semester_name_rx_state_)
  )
}


function Select__root_3c8b680c6efcce43e8348aedc743ae2c () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_fc43cac6d9a225b19126d3c9e8dbcee6 = useCallback(((_ev_0) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.select_semester_by_name", ({ ["name"] : _ev_0 }), ({  })))], [_ev_0], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesSelect.Root,{onValueChange:on_change_fc43cac6d9a225b19126d3c9e8dbcee6,value:reflex___state____state__ptit_reflex___state____conduct_state.selected_semester_name_rx_state_},jsx(RadixThemesSelect.Trigger,{css:({ ["width"] : "320px" })},),jsx(RadixThemesSelect.Content,{},jsx(Select__group_91fe2be0f0af2134f6d6b2335837614e,{},)))
  )
}


function Fragment_0b630256d90782375a7752fe4bfe5e58 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(!((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_evidence"?.valueOf?.()))?(jsx(Fragment,{},jsx(Select__root_3c8b680c6efcce43e8348aedc743ae2c,{},))):(jsx(Fragment,{},))))
  )
}


function Box_8696ab88fa1fc9db2a0dbada4e4c99a9 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    jsx(RadixThemesBox,{css:({ ["width"] : "320px", ["borderRight"] : "1px solid #e5e7eb", ["background"] : "white", ["flexShrink"] : "0" })},jsx(RadixThemesBox,{css:({ ["padding"] : "14px 16px", ["background"] : "#f3f4f6", ["borderBottom"] : "1px solid #e5e7eb", ["textAlign"] : "center" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},"Lo\u1ea1i minh ch\u1ee9ng")),Array.prototype.map.call(reflex___state____state__ptit_reflex___state____conduct_state.evidence_categories_rx_state_ ?? [],((item_rx_state_,index_c6bd694d4a677a97e54a6474dee8c649)=>(jsx(RadixThemesBox,{css:({ ["padding"] : "16px", ["borderBottom"] : "1px solid #e5e7eb", ["borderLeft"] : ((reflex___state____state__ptit_reflex___state____conduct_state.selected_evidence_category_rx_state_?.valueOf?.() === item_rx_state_?.["key"]?.valueOf?.()) ? "4px solid #d92314" : "4px solid transparent"), ["background"] : ((reflex___state____state__ptit_reflex___state____conduct_state.selected_evidence_category_rx_state_?.valueOf?.() === item_rx_state_?.["key"]?.valueOf?.()) ? "#fef2f2" : "white"), ["cursor"] : "pointer" }),key:index_c6bd694d4a677a97e54a6474dee8c649,onClick:((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.select_evidence_category_key", ({ ["category_key"] : item_rx_state_?.["key"] }), ({  })))], [_e], ({  }))))},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["fontWeight"] : ((reflex___state____state__ptit_reflex___state____conduct_state.selected_evidence_category_rx_state_?.valueOf?.() === item_rx_state_?.["key"]?.valueOf?.()) ? "700" : "500"), ["color"] : ((reflex___state____state__ptit_reflex___state____conduct_state.selected_evidence_category_rx_state_?.valueOf?.() === item_rx_state_?.["key"]?.valueOf?.()) ? "#d92314" : "#374151") })},item_rx_state_?.["label"]))))))
  )
}


function Button_89f5ae1b60eab356ad5594275e4a30dc () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_18cce4b39c5a05cb9082be8d7f9c5d77 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.open_evidence_modal", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : "#d92314", ["color"] : "white", ["border"] : "none", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:on_click_18cce4b39c5a05cb9082be8d7f9c5d77},"Th\u00eam m\u1edbi")
  )
}


function Fragment_ea1e6bff2d6db7a16f88816696e81df9 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.can_create_evidence_rx_state_?(jsx(Fragment,{},jsx(Button_89f5ae1b60eab356ad5594275e4a30dc,{},))):(jsx(Fragment,{},))))
  )
}


function Button_c4b809ba8276fba3517b115a4827a629 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_db7dcdf9e0283ea80b432fa6de8a8d2b = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.load", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : "white", ["color"] : "#1f2937", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:on_click_db7dcdf9e0283ea80b432fa6de8a8d2b},"T\u1ea3i l\u1ea1i")
  )
}


function Text_eb35ab60d861402244d1ec721be75434 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#d92314", ["fontWeight"] : "700" })},reflex___state____state__ptit_reflex___state____conduct_state.evidence_count_rx_state_)
  )
}


function Button_9d89a725a5df0988bd04431cb0857f95 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_e0d4cb0639905b4877c1870b8f0af2be = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.toggle_column_config", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : "white", ["color"] : "#1f2937", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 12px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:on_click_e0d4cb0639905b4877c1870b8f0af2be},"\u2699")
  )
}


function Fragment_38b286a6e499dca0364ee966690cf202 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.show_student_code_col_rx_state_?(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["padding"] : "14px 10px", ["borderRight"] : "1px solid #e5e7eb", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["minHeight"] : "48px", ["minWidth"] : "0" })},jsx(RadixThemesText,{as:"p",css:({ ["fontWeight"] : "700" })},"M\u00e3 SV")))):(jsx(Fragment,{},))))
  )
}


function Fragment_dcbf9dcbecf9158d87ba11622ac2b1a4 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.show_full_name_col_rx_state_?(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["padding"] : "14px 10px", ["borderRight"] : "1px solid #e5e7eb", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["minHeight"] : "48px", ["minWidth"] : "0" })},jsx(RadixThemesText,{as:"p",css:({ ["fontWeight"] : "700" })},"H\u1ecd t\u00ean")))):(jsx(Fragment,{},))))
  )
}


function Fragment_add636116e0b73e1eb5b1df43df54628 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.show_class_col_rx_state_?(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["padding"] : "14px 10px", ["borderRight"] : "1px solid #e5e7eb", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["minHeight"] : "48px", ["minWidth"] : "0" })},jsx(RadixThemesText,{as:"p",css:({ ["fontWeight"] : "700" })},"L\u1edbp")))):(jsx(Fragment,{},))))
  )
}


function Fragment_244d069063c8129e719354dde0825696 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.show_reporter_col_rx_state_?(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["padding"] : "14px 10px", ["borderRight"] : "1px solid #e5e7eb", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["minHeight"] : "48px", ["minWidth"] : "0" })},jsx(RadixThemesText,{as:"p",css:({ ["fontWeight"] : "700" })},"Ng\u01b0\u1eddi khai b\u00e1o")))):(jsx(Fragment,{},))))
  )
}


function Fragment_ee6fdbdaf5ee41408703d5b3d6128fd8 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.show_status_col_rx_state_?(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["padding"] : "14px 10px", ["borderRight"] : "1px solid #e5e7eb", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["minHeight"] : "48px", ["minWidth"] : "0" })},jsx(RadixThemesText,{as:"p",css:({ ["fontWeight"] : "700" })},"Tr\u1ea1ng th\u00e1i")))):(jsx(Fragment,{},))))
  )
}


function Fragment_40b55e095034a4d37cc274b3d494345f () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.show_action_col_rx_state_?(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["padding"] : "14px 10px", ["borderRight"] : "none", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["minHeight"] : "48px", ["minWidth"] : "0" })},jsx(RadixThemesText,{as:"p",css:({ ["fontWeight"] : "700" })},"Thao t\u00e1c")))):(jsx(Fragment,{},))))
  )
}


function Box_17d55afa5f7e1a7ea055327efc5179b4 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["display"] : "grid", ["gridTemplateColumns"] : reflex___state____state__ptit_reflex___state____conduct_state.evidence_grid_columns_rx_state_, ["background"] : "#f8fafc" })},jsx(RadixThemesBox,{css:({ ["padding"] : "14px 10px", ["borderRight"] : "1px solid #e5e7eb", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["minHeight"] : "48px", ["minWidth"] : "0" })},jsx(RadixThemesText,{as:"p",css:({ ["fontWeight"] : "700" })},"TT")),jsx(Fragment_38b286a6e499dca0364ee966690cf202,{},),jsx(Fragment_dcbf9dcbecf9158d87ba11622ac2b1a4,{},),jsx(Fragment_add636116e0b73e1eb5b1df43df54628,{},),jsx(Fragment_244d069063c8129e719354dde0825696,{},),jsx(Fragment_ee6fdbdaf5ee41408703d5b3d6128fd8,{},),jsx(Fragment_40b55e095034a4d37cc274b3d494345f,{},))
  )
}


function Flex_c7ae91b98579e3cf3d0a9ae3d92c4317 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"0"},Array.prototype.map.call(reflex___state____state__ptit_reflex___state____conduct_state.evidence_rows_rx_state_ ?? [],((row_rx_state_,index_47253e3ce8f1f75365baf154b184720e)=>(jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["display"] : "grid", ["gridTemplateColumns"] : reflex___state____state__ptit_reflex___state____conduct_state.evidence_grid_columns_rx_state_, ["borderTop"] : "1px solid #e5e7eb", ["background"] : "white" }),key:index_47253e3ce8f1f75365baf154b184720e},jsx(RadixThemesBox,{css:({ ["padding"] : "14px 10px", ["borderRight"] : "1px solid #e5e7eb", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["minHeight"] : "52px", ["minWidth"] : "0" })},jsx(RadixThemesText,{as:"p"},row_rx_state_?.["index"])),jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.show_student_code_col_rx_state_?(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["padding"] : "14px 10px", ["borderRight"] : "1px solid #e5e7eb", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["minHeight"] : "52px", ["minWidth"] : "0" })},jsx(RadixThemesText,{as:"p"},row_rx_state_?.["student_code"])))):(jsx(Fragment,{},)))),jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.show_full_name_col_rx_state_?(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["padding"] : "14px 10px", ["borderRight"] : "1px solid #e5e7eb", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["minHeight"] : "52px", ["minWidth"] : "0" })},jsx(RadixThemesText,{as:"p"},row_rx_state_?.["full_name"])))):(jsx(Fragment,{},)))),jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.show_class_col_rx_state_?(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["padding"] : "14px 10px", ["borderRight"] : "1px solid #e5e7eb", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["minHeight"] : "52px", ["minWidth"] : "0" })},jsx(RadixThemesText,{as:"p"},row_rx_state_?.["class_name"])))):(jsx(Fragment,{},)))),jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.show_reporter_col_rx_state_?(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["padding"] : "14px 10px", ["borderRight"] : "1px solid #e5e7eb", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["minHeight"] : "52px", ["minWidth"] : "0" })},jsx(RadixThemesText,{as:"p"},row_rx_state_?.["reporter_name"])))):(jsx(Fragment,{},)))),jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.show_status_col_rx_state_?(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["padding"] : "14px 10px", ["borderRight"] : "1px solid #e5e7eb", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["minHeight"] : "52px", ["minWidth"] : "0" })},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#d92314", ["fontWeight"] : "600" })},row_rx_state_?.["status_label"])))):(jsx(Fragment,{},)))),jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.show_action_col_rx_state_?(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["padding"] : "14px 10px", ["borderRight"] : "none", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["minHeight"] : "52px", ["minWidth"] : "0" })},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%", ["flexWrap"] : "wrap" }),direction:"row",justify:"center",gap:"2"},jsx(RadixThemesButton,{css:({ ["background"] : "white", ["color"] : "#1f2937", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["height"] : "32px", ["padding"] : "0 12px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.open_evidence_detail", ({ ["evidence_id"] : row_rx_state_?.["id"] }), ({  })))], [_e], ({  }))))},"M\u1edf"),jsx(Fragment,{},(isTrue(row_rx_state_?.["can_delete"])?(jsx(Fragment,{},jsx(RadixThemesButton,{css:({ ["background"] : "#fff1f2", ["color"] : "#d92314", ["border"] : "1px solid #fecdd3", ["borderRadius"] : "8px", ["height"] : "32px", ["padding"] : "0 12px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.remove_evidence", ({ ["evidence_id"] : row_rx_state_?.["id"] }), ({  })))], [_e], ({  }))))},"X\u00f3a"))):(jsx(Fragment,{},)))))))):(jsx(Fragment,{},)))))))))
  )
}


function Fragment_3105c8464f9695214961f79be329256c () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.has_evidence_rows_rx_state_?(jsx(Fragment,{},jsx(Flex_c7ae91b98579e3cf3d0a9ae3d92c4317,{},))):(jsx(Fragment,{},jsx(RadixThemesFlex,{css:({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["minHeight"] : "260px", ["minWidth"] : "900px" })},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",direction:"column",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#9ca3af", ["fontSize"] : "16px", ["fontWeight"] : "500" })},"Kh\u00f4ng c\u00f3 d\u1eef li\u1ec7u"),jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#c0c4cc", ["fontSize"] : "13px" })},"Ch\u01b0a c\u00f3 minh ch\u1ee9ng trong danh m\u1ee5c \u0111ang ch\u1ecdn.")))))))
  )
}


function Text_6e7aef0c2a532a5858f8a47c63530889 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_d5aabbe87afba915a8bee75c36fdcf8d = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.reset_evidence_columns", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#d92314", ["cursor"] : "pointer" }),onClick:on_click_d5aabbe87afba915a8bee75c36fdcf8d},"Kh\u00f4i ph\u1ee5c")
  )
}


function Fragment_f1245419bf8c52a127ba9cfe851d73b4 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.show_student_code_col_rx_state_?(jsx(Fragment,{},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "white", ["fontSize"] : "12px", ["fontWeight"] : "700" })},"\u2713"))):(jsx(Fragment,{},jsx(RadixThemesText,{as:"p"},"")))))
  )
}


function Box_0575d735fbad491f63c93075637d5ed4 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesBox,{css:({ ["width"] : "20px", ["height"] : "20px", ["borderRadius"] : "6px", ["background"] : (reflex___state____state__ptit_reflex___state____conduct_state.show_student_code_col_rx_state_ ? "#d92314" : "white"), ["border"] : "1px solid #d92314", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center" })},jsx(Fragment_f1245419bf8c52a127ba9cfe851d73b4,{},))
  )
}


function Flex_2f31bea14392dd854c228c609a2bddae () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_60eb08637f8e8d02e039d0f409e0c88b = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.toggle_show_student_code_col", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["cursor"] : "pointer" }),direction:"row",onClick:on_click_60eb08637f8e8d02e039d0f409e0c88b,gap:"3"},jsx(Box_0575d735fbad491f63c93075637d5ed4,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["color"] : "#1f2937", ["fontWeight"] : "500" })},"M\u00e3 SV"))
  )
}


function Fragment_e57f3e67e4bc908e1b9633bc8cd5ca69 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.show_full_name_col_rx_state_?(jsx(Fragment,{},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "white", ["fontSize"] : "12px", ["fontWeight"] : "700" })},"\u2713"))):(jsx(Fragment,{},jsx(RadixThemesText,{as:"p"},"")))))
  )
}


function Box_793a43948f8668eb811b6b93cc399644 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesBox,{css:({ ["width"] : "20px", ["height"] : "20px", ["borderRadius"] : "6px", ["background"] : (reflex___state____state__ptit_reflex___state____conduct_state.show_full_name_col_rx_state_ ? "#d92314" : "white"), ["border"] : "1px solid #d92314", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center" })},jsx(Fragment_e57f3e67e4bc908e1b9633bc8cd5ca69,{},))
  )
}


function Flex_03883fd3c19d224723609f74b3370acf () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_88555f7ea0581bd640a03ecec5894a88 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.toggle_show_full_name_col", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["cursor"] : "pointer" }),direction:"row",onClick:on_click_88555f7ea0581bd640a03ecec5894a88,gap:"3"},jsx(Box_793a43948f8668eb811b6b93cc399644,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["color"] : "#1f2937", ["fontWeight"] : "500" })},"H\u1ecd t\u00ean"))
  )
}


function Fragment_f25e564cf19e170876a01c5393b8c8e8 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.show_class_col_rx_state_?(jsx(Fragment,{},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "white", ["fontSize"] : "12px", ["fontWeight"] : "700" })},"\u2713"))):(jsx(Fragment,{},jsx(RadixThemesText,{as:"p"},"")))))
  )
}


function Box_c48278005d964436af37f3c73bf14a9d () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesBox,{css:({ ["width"] : "20px", ["height"] : "20px", ["borderRadius"] : "6px", ["background"] : (reflex___state____state__ptit_reflex___state____conduct_state.show_class_col_rx_state_ ? "#d92314" : "white"), ["border"] : "1px solid #d92314", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center" })},jsx(Fragment_f25e564cf19e170876a01c5393b8c8e8,{},))
  )
}


function Flex_a58f5c3e2a8ce665ddb5ec83e55aa7b8 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_2ac8a4992aaec5bc7aa6789a37a18c81 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.toggle_show_class_col", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["cursor"] : "pointer" }),direction:"row",onClick:on_click_2ac8a4992aaec5bc7aa6789a37a18c81,gap:"3"},jsx(Box_c48278005d964436af37f3c73bf14a9d,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["color"] : "#1f2937", ["fontWeight"] : "500" })},"L\u1edbp"))
  )
}


function Fragment_93e2293441cd15029c3c9fd9c81241b8 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.show_reporter_col_rx_state_?(jsx(Fragment,{},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "white", ["fontSize"] : "12px", ["fontWeight"] : "700" })},"\u2713"))):(jsx(Fragment,{},jsx(RadixThemesText,{as:"p"},"")))))
  )
}


function Box_86a11a921c1fb4eb5e675c3cffc7868f () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesBox,{css:({ ["width"] : "20px", ["height"] : "20px", ["borderRadius"] : "6px", ["background"] : (reflex___state____state__ptit_reflex___state____conduct_state.show_reporter_col_rx_state_ ? "#d92314" : "white"), ["border"] : "1px solid #d92314", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center" })},jsx(Fragment_93e2293441cd15029c3c9fd9c81241b8,{},))
  )
}


function Flex_c2e41f05702b7931113a37c733f076c9 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_ab13f730b70e650a002ee6fc4bc56dec = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.toggle_show_reporter_col", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["cursor"] : "pointer" }),direction:"row",onClick:on_click_ab13f730b70e650a002ee6fc4bc56dec,gap:"3"},jsx(Box_86a11a921c1fb4eb5e675c3cffc7868f,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["color"] : "#1f2937", ["fontWeight"] : "500" })},"Ng\u01b0\u1eddi khai b\u00e1o"))
  )
}


function Fragment_299d77829895455cfa1a3be476a19b14 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.show_status_col_rx_state_?(jsx(Fragment,{},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "white", ["fontSize"] : "12px", ["fontWeight"] : "700" })},"\u2713"))):(jsx(Fragment,{},jsx(RadixThemesText,{as:"p"},"")))))
  )
}


function Box_253aa22cd7f0347f0952b5b364331689 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesBox,{css:({ ["width"] : "20px", ["height"] : "20px", ["borderRadius"] : "6px", ["background"] : (reflex___state____state__ptit_reflex___state____conduct_state.show_status_col_rx_state_ ? "#d92314" : "white"), ["border"] : "1px solid #d92314", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center" })},jsx(Fragment_299d77829895455cfa1a3be476a19b14,{},))
  )
}


function Flex_8feda1c59d63037005aaa20446f1f68a () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_3091d6cc1078ab431e31b02f4cdaa723 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.toggle_show_status_col", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["cursor"] : "pointer" }),direction:"row",onClick:on_click_3091d6cc1078ab431e31b02f4cdaa723,gap:"3"},jsx(Box_253aa22cd7f0347f0952b5b364331689,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["color"] : "#1f2937", ["fontWeight"] : "500" })},"Tr\u1ea1ng th\u00e1i"))
  )
}


function Fragment_b709216780b209cce2082391f1cd9588 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.show_action_col_rx_state_?(jsx(Fragment,{},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "white", ["fontSize"] : "12px", ["fontWeight"] : "700" })},"\u2713"))):(jsx(Fragment,{},jsx(RadixThemesText,{as:"p"},"")))))
  )
}


function Box_b9ad7de1eb38a73a7563ff76775b9586 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesBox,{css:({ ["width"] : "20px", ["height"] : "20px", ["borderRadius"] : "6px", ["background"] : (reflex___state____state__ptit_reflex___state____conduct_state.show_action_col_rx_state_ ? "#d92314" : "white"), ["border"] : "1px solid #d92314", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center" })},jsx(Fragment_b709216780b209cce2082391f1cd9588,{},))
  )
}


function Flex_523d3c8f3ceb2583dd195aa48b60ed9a () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_d16d3abcc5a431e56326b7c3fdd66a0b = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.toggle_show_action_col", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["cursor"] : "pointer" }),direction:"row",onClick:on_click_d16d3abcc5a431e56326b7c3fdd66a0b,gap:"3"},jsx(Box_b9ad7de1eb38a73a7563ff76775b9586,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["color"] : "#1f2937", ["fontWeight"] : "500" })},"Thao t\u00e1c"))
  )
}


function Button_86cdea32a2a0b941932352fc76f4d9b8 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_e0d4cb0639905b4877c1870b8f0af2be = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.toggle_column_config", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : "white", ["color"] : "#1f2937", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:on_click_e0d4cb0639905b4877c1870b8f0af2be},"H\u1ee7y")
  )
}


function Button_806f99b5323205ea346ead8985fa5701 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_e0d4cb0639905b4877c1870b8f0af2be = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.toggle_column_config", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : "#d92314", ["color"] : "white", ["border"] : "none", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:on_click_e0d4cb0639905b4877c1870b8f0af2be},"\u00c1p d\u1ee5ng")
  )
}


function Fragment_f846582f20ef649825a1dafacbb945d6 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.column_config_open_rx_state_?(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["position"] : "absolute", ["top"] : "52px", ["right"] : "0", ["width"] : "320px", ["background"] : "white", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "12px", ["boxShadow"] : "0 18px 40px rgba(15, 23, 42, 0.16)", ["padding"] : "18px", ["zIndex"] : "30" })},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"4"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"row",justify:"between",gap:"3"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "20px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},"C\u1ea5u h\u00ecnh c\u1ed9t"),jsx(Text_6e7aef0c2a532a5858f8a47c63530889,{},)),jsx(Flex_2f31bea14392dd854c228c609a2bddae,{},),jsx(Flex_03883fd3c19d224723609f74b3370acf,{},),jsx(Flex_a58f5c3e2a8ce665ddb5ec83e55aa7b8,{},),jsx(Flex_c2e41f05702b7931113a37c733f076c9,{},),jsx(Flex_8feda1c59d63037005aaa20446f1f68a,{},),jsx(Flex_523d3c8f3ceb2583dd195aa48b60ed9a,{},),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"row",justify:"end",gap:"3"},jsx(Button_86cdea32a2a0b941932352fc76f4d9b8,{},),jsx(Button_806f99b5323205ea346ead8985fa5701,{},)))))):(jsx(Fragment,{},))))
  )
}


function Text_6d0fd67f41c711e476813fd71b49f230 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["fontWeight"] : "700", ["color"] : "white" })},reflex___state____state__ptit_reflex___state____conduct_state.selected_role_management_class_rx_state_)
  )
}


function Button_1f111dcdbb70a51acaae7513683ce318 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_cafcf86d6706b6420c08fe2d713b56a9 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.select_role_management_class", ({ ["class_name"] : "" }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : "white", ["color"] : "#1f2937", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:on_click_cafcf86d6706b6420c08fe2d713b56a9},"Quay l\u1ea1i danh s\u00e1ch l\u1edbp")
  )
}


function Flex_233cfbea99f593137290155e91bc75c6 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"0"},jsx(RadixThemesGrid,{css:({ ["gridTemplateColumns"] : "minmax(280px, 1.8fr) minmax(120px, 0.7fr) minmax(170px, 1fr) minmax(220px, 1.2fr) 150px", ["width"] : "100%", ["background"] : "#f8fafc" })},jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "12px 18px", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "flex-start" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["fontWeight"] : "800", ["color"] : "#6b7280", ["textTransform"] : "uppercase", ["textAlign"] : "left" })},"T\u00ean")),jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "12px 18px", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["fontWeight"] : "800", ["color"] : "#6b7280", ["textTransform"] : "uppercase", ["textAlign"] : "center" })},"M\u00e3")),jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "12px 18px", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["fontWeight"] : "800", ["color"] : "#6b7280", ["textTransform"] : "uppercase", ["textAlign"] : "center" })},"Role")),jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "12px 18px", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["fontWeight"] : "800", ["color"] : "#6b7280", ["textTransform"] : "uppercase", ["textAlign"] : "center" })},"Ph\u00e2n quy\u1ec1n")),jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "12px 18px", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["fontWeight"] : "800", ["color"] : "#6b7280", ["textTransform"] : "uppercase", ["textAlign"] : "center" })},"X\u00f3a t\u00e0i kho\u1ea3n"))),Array.prototype.map.call(reflex___state____state__ptit_reflex___state____conduct_state.filtered_role_management_rows_rx_state_ ?? [],((row_rx_state_,index_47d7fc57ac446a1a69a5d5eb8a15c0e3)=>(jsx(RadixThemesGrid,{css:({ ["gridTemplateColumns"] : "minmax(280px, 1.8fr) minmax(120px, 0.7fr) minmax(170px, 1fr) minmax(220px, 1.2fr) 150px", ["width"] : "100%", ["alignItems"] : "center", ["borderTop"] : "1px solid #e5e7eb", ["background"] : "white" }),key:index_47d7fc57ac446a1a69a5d5eb8a15c0e3},jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "12px 18px" })},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%", ["minWidth"] : "0" }),direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "800", ["color"] : "#1f2937", ["lineHeight"] : "1.4" })},row_rx_state_?.["full_name"]),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["color"] : "#6b7280" })},row_rx_state_?.["username"]),jsx(Fragment,{},(isTrue(row_rx_state_?.["is_self"])?(jsx(Fragment,{},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#92400e", ["fontWeight"] : "700" })},"T\u00e0i kho\u1ea3n hi\u1ec7n t\u1ea1i"))):(jsx(Fragment,{},)))))),jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["padding"] : "12px 8px" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["color"] : "#1f2937", ["fontWeight"] : "600", ["textAlign"] : "center" })},(!((row_rx_state_?.["student_code"]?.valueOf?.() === ""?.valueOf?.())) ? row_rx_state_?.["student_code"] : "\u2014"))),jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["padding"] : "12px 8px" })},jsx(RadixThemesBox,{css:({ ["padding"] : "6px 12px", ["borderRadius"] : "999px", ["background"] : ((row_rx_state_?.["role"]?.valueOf?.() === "admin"?.valueOf?.()) ? "#111827" : ((row_rx_state_?.["role"]?.valueOf?.() === "advisor"?.valueOf?.()) ? "#1d4ed8" : ((row_rx_state_?.["role"]?.valueOf?.() === "class_monitor"?.valueOf?.()) ? "#b45309" : "#047857"))) })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["fontWeight"] : "700", ["color"] : "white" })},row_rx_state_?.["role_label"]))),jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "10px 12px" })},jsx(RadixThemesSelect.Root,{css:({ ["height"] : "40px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : (isTrue(row_rx_state_?.["role_select_disabled"]) ? "#f8fafc" : "white"), ["color"] : "#1f2937", ["fontSize"] : "14px" }),disabled:row_rx_state_?.["role_select_disabled"],key:row_rx_state_?.["id"],onValueChange:((_ev_0) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.assign_role_by_label", ({ ["user_id"] : row_rx_state_?.["id"], ["role_label_text"] : _ev_0 }), ({  })))], [_ev_0], ({  })))),value:row_rx_state_?.["role_label"]},jsx(RadixThemesSelect.Trigger,{css:({ ["width"] : "100%" })},),jsx(RadixThemesSelect.Content,{},jsx(RadixThemesSelect.Group,{},"",Array.prototype.map.call(((reflex___state____state__ptit_reflex___state____conduct_state.current_user_role_rx_state_?.valueOf?.() === "admin"?.valueOf?.()) ? ["Sinh vi\u00ean", "Ban c\u00e1n s\u1ef1", "C\u1ed1 v\u1ea5n h\u1ecdc t\u1eadp", "Admin"] : ["Sinh vi\u00ean", "Ban c\u00e1n s\u1ef1"]) ?? [],((item_rx_state_,index_d6d6157c99650830f12a866606ea87b7)=>(jsx(RadixThemesSelect.Item,{key:index_d6d6157c99650830f12a866606ea87b7,value:item_rx_state_},item_rx_state_)))))))),jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "10px 12px" })},jsx(Fragment,{},(isTrue(row_rx_state_?.["can_delete_account"])?(jsx(Fragment,{},jsx(RadixThemesButton,{css:({ ["background"] : "#fef2f2", ["color"] : "#b91c1c", ["border"] : "1px solid #fca5a5", ["borderRadius"] : "8px", ["height"] : "36px", ["padding"] : "0 12px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.delete_account", ({ ["user_id"] : row_rx_state_?.["id"] }), ({  })))], [_e], ({  }))))},"X\u00f3a t\u00e0i kho\u1ea3n"))):(jsx(Fragment,{},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["color"] : "#6b7280", ["textAlign"] : "center", ["width"] : "100%" })},"\u2014")))))))))))
  )
}


function Fragment_5cb4cb7ab7624016e309cdd4bc297730 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.has_filtered_role_management_rows_rx_state_?(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "12px", ["overflowX"] : "auto", ["background"] : "white" })},jsx(Flex_233cfbea99f593137290155e91bc75c6,{},)))):(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "20px", ["background"] : "white", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "12px" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["color"] : "#6b7280" })},"Kh\u00f4ng c\u00f3 t\u00e0i kho\u1ea3n n\u00e0o trong nh\u00f3m \u0111ang ch\u1ecdn."))))))
  )
}


function Button_8bacf02145855c6bac2388504f4e4a8f () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_9d9b70491f6d986e5c6754229ab83d49 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.select_role_management_class", ({ ["class_name"] : "T\u00e0i kho\u1ea3n h\u1ec7 th\u1ed1ng" }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : "white", ["color"] : "#1f2937", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["height"] : "42px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:on_click_9d9b70491f6d986e5c6754229ab83d49},"T\u00e0i kho\u1ea3n h\u1ec7 th\u1ed1ng")
  )
}


function Fragment_9ff25d64bba10a8c67956dcef5222f55 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},((reflex___state____state__ptit_reflex___state____conduct_state.current_user_role_rx_state_?.valueOf?.() === "admin"?.valueOf?.())?(jsx(Fragment,{},jsx(Button_8bacf02145855c6bac2388504f4e4a8f,{},))):(jsx(Fragment,{},))))
  )
}


function Text_9876f327f11bc086eebcb39dcb3fd674 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["color"] : "#6b7280", ["lineHeight"] : "1.7" })},((reflex___state____state__ptit_reflex___state____conduct_state.current_user_role_rx_state_?.valueOf?.() === "admin"?.valueOf?.()) ? "Ch\u1ecdn m\u1ed9t l\u1edbp \u0111\u1ec3 m\u1edf danh s\u00e1ch t\u00e0i kho\u1ea3n trong l\u1edbp \u0111\u00f3. T\u00e0i kho\u1ea3n h\u1ec7 th\u1ed1ng \u0111\u01b0\u1ee3c t\u00e1ch ri\u00eang \u1edf g\u00f3c ph\u1ea3i." : "C\u1ed1 v\u1ea5n h\u1ecdc t\u1eadp ch\u1ec9 \u0111\u01b0\u1ee3c \u0111\u1ed5i quy\u1ec1n gi\u1eefa Sinh vi\u00ean v\u00e0 Ban c\u00e1n s\u1ef1 trong l\u1edbp m\u00ecnh ph\u1ee5 tr\u00e1ch."))
  )
}


function Flex_cdae06de356a5512b7660a12c4730bb8 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"3"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["fontWeight"] : "800", ["color"] : "#6b7280", ["textTransform"] : "uppercase" })},"Danh s\u00e1ch l\u1edbp"),Array.prototype.map.call(reflex___state____state__ptit_reflex___state____conduct_state.role_management_class_groups_rx_state_ ?? [],((class_name_rx_state_,index_3c719b5e161cc3b12b485f7f64ee3c5b)=>(jsx(RadixThemesButton,{css:({ ["background"] : ((reflex___state____state__ptit_reflex___state____conduct_state.selected_role_management_class_rx_state_?.valueOf?.() === class_name_rx_state_?.valueOf?.()) ? "#d92314" : "white"), ["color"] : ((reflex___state____state__ptit_reflex___state____conduct_state.selected_role_management_class_rx_state_?.valueOf?.() === class_name_rx_state_?.valueOf?.()) ? "white" : "#1f2937"), ["border"] : ((reflex___state____state__ptit_reflex___state____conduct_state.selected_role_management_class_rx_state_?.valueOf?.() === class_name_rx_state_?.valueOf?.()) ? "none" : "1px solid #e5e7eb"), ["borderRadius"] : "12px", ["padding"] : "0 18px", ["height"] : "54px", ["width"] : "100%", ["fontSize"] : "15px", ["fontWeight"] : ((reflex___state____state__ptit_reflex___state____conduct_state.selected_role_management_class_rx_state_?.valueOf?.() === class_name_rx_state_?.valueOf?.()) ? "700" : "600"), ["cursor"] : "pointer", ["boxShadow"] : "none", ["justifyContent"] : "flex-start" }),key:index_3c719b5e161cc3b12b485f7f64ee3c5b,onClick:((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.select_role_management_class", ({ ["class_name"] : class_name_rx_state_ }), ({  })))], [_e], ({  }))))},class_name_rx_state_)))))
  )
}


function Fragment_969b3e8f37bbea9ea6150bc28fece0f7 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.role_management_has_selection_rx_state_?(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"4"},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["flexWrap"] : "wrap" }),direction:"row",justify:"between",gap:"3"},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["flexWrap"] : "wrap" }),direction:"row",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["color"] : "#6b7280", ["fontWeight"] : "600" })},"\u0110ang hi\u1ec3n th\u1ecb:"),jsx(RadixThemesBox,{css:({ ["padding"] : "6px 12px", ["borderRadius"] : "999px", ["background"] : "#111827" })},jsx(Text_6d0fd67f41c711e476813fd71b49f230,{},))),jsx(Button_1f111dcdbb70a51acaae7513683ce318,{},)),jsx(Fragment_5cb4cb7ab7624016e309cdd4bc297730,{},)))):(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"4"},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["flexWrap"] : "wrap" }),direction:"row",justify:"between",gap:"3"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "22px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},"Qu\u1ea3n l\u00fd t\u00e0i kho\u1ea3n"),jsx(Fragment_9ff25d64bba10a8c67956dcef5222f55,{},)),jsx(Text_9876f327f11bc086eebcb39dcb3fd674,{},),jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "18px", ["background"] : "white", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "12px" })},jsx(Flex_cdae06de356a5512b7660a12c4730bb8,{},)))))))
  )
}


function Select__root_2eb61b77968297c73d413c56ca84877e () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_fc43cac6d9a225b19126d3c9e8dbcee6 = useCallback(((_ev_0) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.select_semester_by_name", ({ ["name"] : _ev_0 }), ({  })))], [_ev_0], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesSelect.Root,{onValueChange:on_change_fc43cac6d9a225b19126d3c9e8dbcee6,value:reflex___state____state__ptit_reflex___state____conduct_state.selected_semester_name_rx_state_},jsx(RadixThemesSelect.Trigger,{css:({ ["width"] : "100%" })},),jsx(RadixThemesSelect.Content,{},jsx(Select__group_91fe2be0f0af2134f6d6b2335837614e,{},)))
  )
}


function Debounceinput_dedb5ad75083a8c755ea33a4bf6577d3 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_62751b52701a3322124fc6fddb6389d3 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "admin_stage_0_label", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_62751b52701a3322124fc6fddb6389d3,placeholder:"V\u00ed d\u1ee5: Sinh vi\u00ean \u0111\u00e1nh gi\u00e1",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.admin_stage_0_label_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.admin_stage_0_label_rx_state_ : "")},)
  )
}


function Debounceinput_c3e2af26f1bf359873bc11831bf2b1d3 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_ca8878b57d510134b47b08cbd9d3212f = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "admin_stage_0_start", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_ca8878b57d510134b47b08cbd9d3212f,placeholder:"01/02/2026 00:00",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.admin_stage_0_start_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.admin_stage_0_start_rx_state_ : "")},)
  )
}


function Debounceinput_daf033754fdc96e29f2b5b43ae984669 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_e4f2b747ba701bb1e52df0a8dcbc5e90 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "admin_stage_0_end", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_e4f2b747ba701bb1e52df0a8dcbc5e90,placeholder:"31/07/2026 23:45",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.admin_stage_0_end_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.admin_stage_0_end_rx_state_ : "")},)
  )
}


function Debounceinput_6439f12b3467d556bd23463a3439eda4 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_f50d75d6aed35bb7960589fd2192da12 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "admin_stage_1_label", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_f50d75d6aed35bb7960589fd2192da12,placeholder:"V\u00ed d\u1ee5: Sinh vi\u00ean \u0111\u00e1nh gi\u00e1",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.admin_stage_1_label_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.admin_stage_1_label_rx_state_ : "")},)
  )
}


function Debounceinput_bf50115578fe612e9471ee4a4b7c73bd () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_7aea7909868dbbf49079148c1de84b10 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "admin_stage_1_start", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_7aea7909868dbbf49079148c1de84b10,placeholder:"01/02/2026 00:00",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.admin_stage_1_start_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.admin_stage_1_start_rx_state_ : "")},)
  )
}


function Debounceinput_2848184a3d2ce468f0c366ff1b130f72 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_d61050650f58b0baa45a7dbd97e587f1 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "admin_stage_1_end", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_d61050650f58b0baa45a7dbd97e587f1,placeholder:"31/07/2026 23:45",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.admin_stage_1_end_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.admin_stage_1_end_rx_state_ : "")},)
  )
}


function Debounceinput_9b3e6ea3c74988dc5146a695f224f1d0 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_408dd1d5e910c5918e7abe0ac3470af5 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "admin_stage_2_label", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_408dd1d5e910c5918e7abe0ac3470af5,placeholder:"V\u00ed d\u1ee5: Sinh vi\u00ean \u0111\u00e1nh gi\u00e1",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.admin_stage_2_label_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.admin_stage_2_label_rx_state_ : "")},)
  )
}


function Debounceinput_529381a8331ab04c3133da63b9591df4 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_87914a94c77597815b99ca87691004a8 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "admin_stage_2_start", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_87914a94c77597815b99ca87691004a8,placeholder:"01/02/2026 00:00",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.admin_stage_2_start_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.admin_stage_2_start_rx_state_ : "")},)
  )
}


function Debounceinput_8d47fd8d9a35f2a947dd50ef40aefbc9 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_36a235618981a1bf88cddd70fdff1b6c = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "admin_stage_2_end", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_36a235618981a1bf88cddd70fdff1b6c,placeholder:"31/07/2026 23:45",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.admin_stage_2_end_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.admin_stage_2_end_rx_state_ : "")},)
  )
}


function Debounceinput_0258db4794ec6235d32d1510fd89239b () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_6ba2870cc2bde3ff5fdd73856f885ca8 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "admin_stage_3_label", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_6ba2870cc2bde3ff5fdd73856f885ca8,placeholder:"V\u00ed d\u1ee5: Sinh vi\u00ean \u0111\u00e1nh gi\u00e1",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.admin_stage_3_label_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.admin_stage_3_label_rx_state_ : "")},)
  )
}


function Debounceinput_ceceba24488b7b7cc66e5fdff8873095 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_ad3162dda10c8495ec3c22cc6e8e45c7 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "admin_stage_3_start", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_ad3162dda10c8495ec3c22cc6e8e45c7,placeholder:"01/02/2026 00:00",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.admin_stage_3_start_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.admin_stage_3_start_rx_state_ : "")},)
  )
}


function Debounceinput_fcf915094685af3c646bdae145cd5096 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_33fa7008621f986a9dccecb42eb75c71 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "admin_stage_3_end", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_33fa7008621f986a9dccecb42eb75c71,placeholder:"31/07/2026 23:45",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.admin_stage_3_end_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.admin_stage_3_end_rx_state_ : "")},)
  )
}


function Button_a6fad7ce98ee048de4481db700297603 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_7aba95d16a2c1d2954d3456ce3e2b0e7 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.save_admin_stage_windows", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : "#d92314", ["color"] : "white", ["border"] : "none", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:on_click_7aba95d16a2c1d2954d3456ce3e2b0e7},"L\u01b0u m\u1ed1c th\u1eddi gian")
  )
}


function Flex_f55c0c1875513805711ebf42d0626700 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"4"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "18px", ["fontWeight"] : "800", ["color"] : "#1f2937" })},"\u0110\u0103ng k\u00fd s\u1ef1 ki\u1ec7n"),Array.prototype.map.call(reflex___state____state__ptit_reflex___state____conduct_state.open_events_rx_state_ ?? [],((item_rx_state_,index_377cb87b52b1ed0d6aca5fbbdea4588e)=>(jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["background"] : "white", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "10px", ["padding"] : "14px", ["flexWrap"] : "wrap" }),direction:"row",justify:"between",key:index_377cb87b52b1ed0d6aca5fbbdea4588e,gap:"3"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["cursor"] : "pointer" }),direction:"column",onClick:((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.open_event_detail", ({ ["event_id"] : item_rx_state_?.["id"] }), ({  })))], [_e], ({  })))),gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},item_rx_state_?.["title"]),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["color"] : "#6b7280" })},item_rx_state_?.["start_time"]),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["color"] : "#6b7280" })},item_rx_state_?.["location"])),jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",direction:"row",gap:"3"},jsx(RadixThemesBox,{css:({ ["background"] : "#fff7ed", ["borderRadius"] : "999px", ["padding"] : "6px 12px" })},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",direction:"row",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["fontWeight"] : "700", ["color"] : "#c2410c" })},"+"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["fontWeight"] : "700", ["color"] : "#c2410c" })},item_rx_state_?.["points"]),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["fontWeight"] : "700", ["color"] : "#c2410c" })},"\u0111i\u1ec3m t\u1ed1i \u0111a"))),jsx(Fragment,{},(isTrue(item_rx_state_?.["can_register"])?(jsx(Fragment,{},jsx(RadixThemesButton,{css:({ ["background"] : "#d92314", ["color"] : "white", ["border"] : "none", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.register_event", ({ ["event_id"] : item_rx_state_?.["id"] }), ({  })))], [_e], ({  }))))},"\u0110\u0103ng k\u00fd"))):(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["padding"] : "6px 12px", ["borderRadius"] : "999px", ["background"] : "#f3f4f6" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},"Ch\u1ec9 sinh vi\u00ean m\u1edbi \u0111\u0103ng k\u00fd"))))))))))))
  )
}


function Fragment_3313b9eb59c5533bd4461176aeb5b41b () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.has_open_events_rx_state_?(jsx(Fragment,{},jsx(Flex_f55c0c1875513805711ebf42d0626700,{},))):(jsx(Fragment,{},))))
  )
}


function Text_31c06235269defc03ec22243c13cfe7b () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : ((reflex___state____state__ptit_reflex___state____conduct_state.event_tab_rx_state_?.valueOf?.() === "joined"?.valueOf?.()) ? "#1f2937" : "#6b7280"), ["fontWeight"] : ((reflex___state____state__ptit_reflex___state____conduct_state.event_tab_rx_state_?.valueOf?.() === "joined"?.valueOf?.()) ? "700" : "500"), ["fontSize"] : "14px" })},"\u0110\u00e3 tham gia")
  )
}


function Box_1e2870834b5f056d773bbab4f2d14835 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_478a698623ff9f3cd2d032c1c072f9fd = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.select_event_tab", ({ ["tab"] : "joined" }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesBox,{css:({ ["padding"] : "8px 14px", ["background"] : ((reflex___state____state__ptit_reflex___state____conduct_state.event_tab_rx_state_?.valueOf?.() === "joined"?.valueOf?.()) ? "white" : "transparent"), ["borderRadius"] : "6px", ["boxShadow"] : ((reflex___state____state__ptit_reflex___state____conduct_state.event_tab_rx_state_?.valueOf?.() === "joined"?.valueOf?.()) ? "0 1px 3px rgba(0, 0, 0, 0.08)" : "none"), ["cursor"] : "pointer" }),onClick:on_click_478a698623ff9f3cd2d032c1c072f9fd},jsx(Text_31c06235269defc03ec22243c13cfe7b,{},))
  )
}


function Text_ae873a562fe2cf6e47a04f46a150ca65 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : ((reflex___state____state__ptit_reflex___state____conduct_state.event_tab_rx_state_?.valueOf?.() === "registered"?.valueOf?.()) ? "#1f2937" : "#6b7280"), ["fontWeight"] : ((reflex___state____state__ptit_reflex___state____conduct_state.event_tab_rx_state_?.valueOf?.() === "registered"?.valueOf?.()) ? "700" : "500"), ["fontSize"] : "14px" })},"\u0110\u00e3 \u0111\u0103ng k\u00fd")
  )
}


function Box_3d012a9cfabaabb08abe34e9d12811db () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_d034f75dea7e22e47a2edde7a20c4a2b = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.select_event_tab", ({ ["tab"] : "registered" }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesBox,{css:({ ["padding"] : "8px 14px", ["background"] : ((reflex___state____state__ptit_reflex___state____conduct_state.event_tab_rx_state_?.valueOf?.() === "registered"?.valueOf?.()) ? "white" : "transparent"), ["borderRadius"] : "6px", ["boxShadow"] : ((reflex___state____state__ptit_reflex___state____conduct_state.event_tab_rx_state_?.valueOf?.() === "registered"?.valueOf?.()) ? "0 1px 3px rgba(0, 0, 0, 0.08)" : "none"), ["cursor"] : "pointer" }),onClick:on_click_d034f75dea7e22e47a2edde7a20c4a2b},jsx(Text_ae873a562fe2cf6e47a04f46a150ca65,{},))
  )
}


function Flex_8aa456fde7170720ee3cee6bb3245d74 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"5"},Array.prototype.map.call(reflex___state____state__ptit_reflex___state____conduct_state.joined_events_rx_state_ ?? [],((item_rx_state_,index_96a75bd8539756e4da3b5311a92772c2)=>(jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",key:index_96a75bd8539756e4da3b5311a92772c2,gap:"2"},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",direction:"row",gap:"3"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["color"] : "#6b7280", ["fontWeight"] : "600" })},item_rx_state_?.["date"]),jsx(RadixThemesBox,{css:({ ["minWidth"] : "16px", ["height"] : "16px", ["borderRadius"] : "999px", ["background"] : "#ef4444", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["padding"] : "0 4px" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "10px", ["color"] : "white", ["fontWeight"] : "700" })},item_rx_state_?.["count"]))),jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["background"] : "#f8fafc", ["border"] : "1px solid #f1f5f9", ["borderRadius"] : "8px", ["padding"] : "12px 14px", ["width"] : "100%", ["cursor"] : "pointer" }),direction:"row",onClick:((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.open_event_detail", ({ ["event_id"] : item_rx_state_?.["id"] }), ({  })))], [_e], ({  })))),gap:"4"},jsx(RadixThemesText,{as:"p",css:({ ["width"] : "56px", ["textAlign"] : "right", ["fontSize"] : "14px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},item_rx_state_?.["time"]),jsx(RadixThemesBox,{css:({ ["width"] : "4px", ["minHeight"] : "36px", ["borderRadius"] : "999px", ["background"] : item_rx_state_?.["accent"] })},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["color"] : "#374151", ["flex"] : "1" })},item_rx_state_?.["title"])))))))
  )
}


function Fragment_cfbdd1fd8145c5ef8f0ff9ac93bd45e4 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(!((reflex___state____state__ptit_reflex___state____conduct_state.joined_events_rx_state_?.valueOf?.() === []?.valueOf?.()))?(jsx(Fragment,{},jsx(Flex_8aa456fde7170720ee3cee6bb3245d74,{},))):(jsx(Fragment,{},jsx(RadixThemesFlex,{css:({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["minHeight"] : "180px" })},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#9ca3af", ["fontSize"] : "15px", ["fontWeight"] : "500" })},"Ch\u01b0a c\u00f3 s\u1ef1 ki\u1ec7n n\u00e0o \u0111\u01b0\u1ee3c duy\u1ec7t l\u00e0 \u0111\u00e3 tham gia."))))))
  )
}


function Flex_a709ecea0e2b31c4d2bb513e568aada4 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"4"},Array.prototype.map.call(reflex___state____state__ptit_reflex___state____conduct_state.registered_events_rx_state_ ?? [],((item_rx_state_,index_558cc69d90d6ea07a1c9a91620137414)=>(jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["background"] : "#f8fafc", ["border"] : "1px solid #f1f5f9", ["borderRadius"] : "8px", ["padding"] : "14px" }),direction:"row",justify:"between",key:index_558cc69d90d6ea07a1c9a91620137414,gap:"3"},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["cursor"] : "pointer" }),direction:"row",onClick:((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.open_event_detail", ({ ["event_id"] : item_rx_state_?.["id"] }), ({  })))], [_e], ({  })))),gap:"4"},jsx(RadixThemesBox,{css:({ ["width"] : "4px", ["minHeight"] : "42px", ["borderRadius"] : "999px", ["background"] : "#53b8dc" })},),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "600", ["color"] : "#1f2937" })},item_rx_state_?.["title"]),jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",direction:"row",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["color"] : "#6b7280" })},"C\u1ed9ng"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["color"] : "#6b7280", ["fontWeight"] : "700" })},item_rx_state_?.["points"]),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["color"] : "#6b7280" })},"\u0111i\u1ec3m")),jsx(Fragment,{},(!((item_rx_state_?.["status_label"]?.valueOf?.() === ""?.valueOf?.()))?(jsx(Fragment,{},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#d92314", ["fontWeight"] : "700" })},item_rx_state_?.["status_label"]))):(jsx(Fragment,{},)))))),jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",direction:"row",gap:"3"},jsx(RadixThemesButton,{css:({ ["background"] : "white", ["color"] : "#1f2937", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.open_event_detail", ({ ["event_id"] : item_rx_state_?.["id"] }), ({  })))], [_e], ({  }))))},"Chi ti\u1ebft"),jsx(Fragment,{},(isTrue(item_rx_state_?.["can_approve"])?(jsx(Fragment,{},jsx(RadixThemesButton,{css:({ ["background"] : "#15803d", ["color"] : "white", ["border"] : "none", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.approve_event", ({ ["participation_id"] : item_rx_state_?.["participation_id"] }), ({  })))], [_e], ({  }))))},"Duy\u1ec7t"))):(jsx(Fragment,{},)))),jsx(RadixThemesBox,{css:({ ["padding"] : "6px 12px", ["borderRadius"] : "999px", ["background"] : "#f3f4f6" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},item_rx_state_?.["action_label"]))))))))
  )
}


function Fragment_b73b99f74df1e6e35b448897bf6ab30d () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.has_registered_events_rx_state_?(jsx(Fragment,{},jsx(Flex_a709ecea0e2b31c4d2bb513e568aada4,{},))):(jsx(Fragment,{},jsx(RadixThemesFlex,{css:({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["minHeight"] : "180px" })},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#9ca3af", ["fontSize"] : "15px", ["fontWeight"] : "500" })},"Ch\u01b0a c\u00f3 \u0111\u0103ng k\u00fd s\u1ef1 ki\u1ec7n n\u00e0o."))))))
  )
}


function Fragment_ff20d0eda704f84f6f3ecc3c6bc8e216 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},((reflex___state____state__ptit_reflex___state____conduct_state.event_tab_rx_state_?.valueOf?.() === "joined"?.valueOf?.())?(jsx(Fragment_cfbdd1fd8145c5ef8f0ff9ac93bd45e4,{},)):(jsx(Fragment_b73b99f74df1e6e35b448897bf6ab30d,{},))))
  )
}


function Select__root_75a33be3164c7fddda54a3c0dee52d8b () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_ed37ad4bb3b38b97aa5e068b78a3d775 = useCallback(((_ev_0) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.select_admin_new_event_semester", ({ ["name"] : _ev_0 }), ({  })))], [_ev_0], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesSelect.Root,{onValueChange:on_change_ed37ad4bb3b38b97aa5e068b78a3d775,value:reflex___state____state__ptit_reflex___state____conduct_state.admin_new_event_semester_name_rx_state_},jsx(RadixThemesSelect.Trigger,{css:({ ["width"] : "100%" })},),jsx(RadixThemesSelect.Content,{},jsx(Select__group_91fe2be0f0af2134f6d6b2335837614e,{},)))
  )
}


function Select__group_45e13e525cfd521feb7f019e76e222e1 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesSelect.Group,{},"",Array.prototype.map.call(reflex___state____state__ptit_reflex___state____conduct_state.criterion_choice_labels_rx_state_ ?? [],((item_rx_state_,index_d6d6157c99650830f12a866606ea87b7)=>(jsx(RadixThemesSelect.Item,{key:index_d6d6157c99650830f12a866606ea87b7,value:item_rx_state_},item_rx_state_)))))
  )
}


function Select__root_27665ec93a769bfc897f18c6a00ab102 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_0b771d26298f36fd8caaf6e11f2f7358 = useCallback(((_ev_0) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "admin_event_criterion_choice", ["value"] : _ev_0 }), ({  })))], [_ev_0], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesSelect.Root,{onValueChange:on_change_0b771d26298f36fd8caaf6e11f2f7358,value:reflex___state____state__ptit_reflex___state____conduct_state.admin_event_criterion_choice_rx_state_},jsx(RadixThemesSelect.Trigger,{css:({ ["width"] : "100%" })},),jsx(RadixThemesSelect.Content,{},jsx(Select__group_45e13e525cfd521feb7f019e76e222e1,{},)))
  )
}


function Debounceinput_f9585af75e7df0e7d2f9ac5c50ed3e65 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_acc7e0de2ecc94b72e90d82a71bfb6ba = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "admin_new_event_name", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_acc7e0de2ecc94b72e90d82a71bfb6ba,placeholder:"V\u00ed d\u1ee5: Ng\u00e0y h\u1ed9i vi\u1ec7c l\u00e0m ATTT 2026",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.admin_new_event_name_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.admin_new_event_name_rx_state_ : "")},)
  )
}


function Debounceinput_a8f0e3a5c61216540f9615a06dfd95a3 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_10b55e0c57b6b5656733330ca34cc459 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "admin_new_event_start_time", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_10b55e0c57b6b5656733330ca34cc459,placeholder:"Ch\u1ecdn th\u1eddi gian b\u1eaft \u0111\u1ea7u",type:"datetime-local",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.admin_new_event_start_time_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.admin_new_event_start_time_rx_state_ : "")},)
  )
}


function Debounceinput_d3273f05204672b3e8579c0989b39491 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_757f49e2b9b7f6a921b3e4b57d0e3c83 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "admin_new_event_end_time", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_757f49e2b9b7f6a921b3e4b57d0e3c83,placeholder:"Ch\u1ecdn th\u1eddi gian k\u1ebft th\u00fac",type:"datetime-local",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.admin_new_event_end_time_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.admin_new_event_end_time_rx_state_ : "")},)
  )
}


function Debounceinput_eb4c4f95bbf80b01aaae4a92bd2df201 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_64d582ee6279226046bc02dd25291036 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "admin_new_event_location", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_64d582ee6279226046bc02dd25291036,placeholder:"V\u00ed d\u1ee5: H\u1ed9i tr\u01b0\u1eddng A2, c\u01a1 s\u1edf H\u00e0 \u0110\u00f4ng",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.admin_new_event_location_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.admin_new_event_location_rx_state_ : "")},)
  )
}


function Debounceinput_5711941a38c137cc50aea192e5507487 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_d90c4f194bc84531ef6effc99d950643 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "admin_new_event_points", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_d90c4f194bc84531ef6effc99d950643,placeholder:"1",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.admin_new_event_points_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.admin_new_event_points_rx_state_ : "")},)
  )
}


function Button_9bcdcb30145bee0da6ceb2cdac038939 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_ffb657823bca10a3f1909ad61a99cc29 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.submit_admin_event", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : "#d92314", ["color"] : "white", ["border"] : "none", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:on_click_ffb657823bca10a3f1909ad61a99cc29},"T\u1ea1o s\u1ef1 ki\u1ec7n")
  )
}


function Debounceinput_214c1d76a9e3c638f421e3e87eccf285 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_3a7ee87d7797c44a94bf943ebecb8d95 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_student_list_filter", ({ ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["maxWidth"] : "520px", ["height"] : "40px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["paddingLeft"] : "12px", ["paddingRight"] : "12px" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_3a7ee87d7797c44a94bf943ebecb8d95,placeholder:"L\u1ecdc theo t\u00ean, m\u00e3 SV, \u0111i\u1ec3m ho\u1eb7c x\u1ebfp lo\u1ea1i\u2026",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.student_list_filter_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.student_list_filter_rx_state_ : "")},)
  )
}


function Flex_cc6906835f6e8ffb286333af349ae142 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"3"},Array.prototype.map.call(reflex___state____state__ptit_reflex___state____conduct_state.filtered_students_rx_state_ ?? [],((row_rx_state_,index_358d7e418428a6982de9a76b75835c93)=>(jsx(RadixThemesBox,{css:({ ["padding"] : "16px 18px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "10px", ["background"] : "white", ["width"] : "100%", ["&:hover"] : ({ ["background"] : "#f9fafb" }) }),key:row_rx_state_?.["id"]},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["flexWrap"] : "wrap" }),direction:"row",justify:"between",gap:"3"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "700", ["color"] : "#1f2937", ["cursor"] : "pointer" }),onClick:((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.pick_student_open_info", ({ ["label"] : row_rx_state_?.["label"] }), ({  })))], [_e], ({  }))))},row_rx_state_?.["label"]),jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["flexWrap"] : "wrap" }),direction:"row",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["fontWeight"] : "700", ["color"] : "#6b7280" })},"\u0110i\u1ec3m:"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["fontWeight"] : "700", ["color"] : "#92400e" })},row_rx_state_?.["score_total"]),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280" })},"\u2022"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["fontWeight"] : "700", ["color"] : "#0369a1" })},row_rx_state_?.["conduct_grade"]))),jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["flexWrap"] : "wrap" }),direction:"row",justify:"end",gap:"3"},jsx(RadixThemesButton,{css:({ ["background"] : "white", ["color"] : "#1f2937", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.pick_student_open_score", ({ ["label"] : row_rx_state_?.["label"] }), ({  })))], [_e], ({  }))))},"Xem phi\u1ebfu \u0111i\u1ec3m r\u00e8n luy\u1ec7n"))))))))
  )
}


function Flex_314aef5b530c1551124c602e2b17f867 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"3"},Array.prototype.map.call(reflex___state____state__ptit_reflex___state____conduct_state.filtered_students_rx_state_ ?? [],((row_rx_state_,index_ee8ad832e87c44abac328dacb21abcbc)=>(jsx(RadixThemesBox,{css:({ ["padding"] : "18px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "12px", ["background"] : "white", ["width"] : "100%", ["&:hover"] : ({ ["background"] : "#f9fafb" }) }),key:row_rx_state_?.["id"]},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["flexWrap"] : "wrap" }),direction:"row",justify:"between",gap:"4"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "0" }),direction:"column",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "16px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},row_rx_state_?.["full_name"]),jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["flexWrap"] : "wrap" }),direction:"row",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["color"] : "#6b7280" })},row_rx_state_?.["student_code"]),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["color"] : "#6b7280" })},"\u2022"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["color"] : "#6b7280" })},row_rx_state_?.["class_name"])),jsx(RadixThemesBox,{css:({ ["padding"] : "6px 12px", ["borderRadius"] : "999px", ["background"] : "#f0fdf4" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["fontWeight"] : "700", ["color"] : "#166534" })},row_rx_state_?.["conduct_grade"]))),jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["flexWrap"] : "wrap" }),direction:"row",justify:"end",gap:"3"},jsx(RadixThemesBox,{css:({ ["background"] : "#fffbeb", ["borderRadius"] : "999px", ["padding"] : "6px 12px" })},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",direction:"row",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["fontWeight"] : "700", ["color"] : "#92400e" })},"\u0110i\u1ec3m:"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["fontWeight"] : "700", ["color"] : "#92400e" })},row_rx_state_?.["score_total"]))),jsx(RadixThemesButton,{css:({ ["background"] : "white", ["color"] : "#1f2937", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.pick_student_open_score", ({ ["label"] : row_rx_state_?.["label"] }), ({  })))], [_e], ({  }))))},"Xem phi\u1ebfu \u0111i\u1ec3m r\u00e8n luy\u1ec7n"))))))))
  )
}


function Flex_86f572b2e186b8a68a05d61b4609d792 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"3"},Array.prototype.map.call(reflex___state____state__ptit_reflex___state____conduct_state.filtered_students_rx_state_ ?? [],((row_rx_state_,index_ce4365f480ff76f27e16edfa0813a715)=>(jsx(RadixThemesBox,{css:({ ["padding"] : "18px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "12px", ["background"] : "white", ["width"] : "100%", ["&:hover"] : ({ ["background"] : "#f9fafb" }) }),key:row_rx_state_?.["id"]},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["flexWrap"] : "wrap" }),direction:"row",justify:"between",gap:"4"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "0" }),direction:"column",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "16px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},row_rx_state_?.["full_name"]),jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["flexWrap"] : "wrap" }),direction:"row",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["color"] : "#6b7280" })},row_rx_state_?.["student_code"]),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["color"] : "#6b7280" })},"\u2022"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["color"] : "#6b7280" })},row_rx_state_?.["class_name"])),jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",direction:"row",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["fontWeight"] : "600", ["color"] : "#9a3412" })},"Minh ch\u1ee9ng ch\u1edd duy\u1ec7t:"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["fontWeight"] : "700", ["color"] : "#9a3412" })},row_rx_state_?.["pending_evidence_count"]))),jsx(RadixThemesButton,{css:({ ["background"] : "white", ["color"] : "#1f2937", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.pick_student_open_evidence", ({ ["label"] : row_rx_state_?.["label"] }), ({  })))], [_e], ({  }))))},"M\u1edf duy\u1ec7t minh ch\u1ee9ng")))))))
  )
}


function Flex_757262c88f28240466c44c37c9372c98 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"3"},Array.prototype.map.call(reflex___state____state__ptit_reflex___state____conduct_state.filtered_students_rx_state_ ?? [],((row_rx_state_,index_ce4365f480ff76f27e16edfa0813a715)=>(jsx(RadixThemesBox,{css:({ ["padding"] : "18px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "12px", ["background"] : "white", ["width"] : "100%", ["&:hover"] : ({ ["background"] : "#f9fafb" }) }),key:row_rx_state_?.["id"]},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["flexWrap"] : "wrap" }),direction:"row",justify:"between",gap:"4"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["minWidth"] : "0" }),direction:"column",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "16px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},row_rx_state_?.["full_name"]),jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["flexWrap"] : "wrap" }),direction:"row",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["color"] : "#6b7280" })},row_rx_state_?.["student_code"]),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["color"] : "#6b7280" })},"\u2022"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["color"] : "#6b7280" })},row_rx_state_?.["class_name"])),jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",direction:"row",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["fontWeight"] : "600", ["color"] : "#9a3412" })},"S\u1ef1 ki\u1ec7n ch\u1edd duy\u1ec7t:"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["fontWeight"] : "700", ["color"] : "#9a3412" })},row_rx_state_?.["pending_event_count"]))),jsx(RadixThemesButton,{css:({ ["background"] : "white", ["color"] : "#1f2937", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.pick_student_open_events", ({ ["label"] : row_rx_state_?.["label"] }), ({  })))], [_e], ({  }))))},"M\u1edf duy\u1ec7t s\u1ef1 ki\u1ec7n")))))))
  )
}


function Fragment_84eda3506f28e66b6de13fda6a2ae187 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.has_registered_events_rx_state_?(jsx(Fragment,{},jsx(Flex_a709ecea0e2b31c4d2bb513e568aada4,{},))):(jsx(Fragment,{},jsx(RadixThemesFlex,{css:({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["minHeight"] : "180px" })},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#9ca3af", ["fontSize"] : "15px", ["fontWeight"] : "500" })},"Sinh vi\u00ean n\u00e0y ch\u01b0a c\u00f3 \u0111\u0103ng k\u00fd s\u1ef1 ki\u1ec7n n\u00e0o."))))))
  )
}


function Flex_6d27a14838fa9b4ecd4b33e914d5c3da () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"row",gap:"0"},Array.prototype.map.call(reflex___state____state__ptit_reflex___state____conduct_state.timeline_rx_state_ ?? [],((item_rx_state_,index_88bde4c6288affda480f97a1eded32d0)=>(jsx(RadixThemesBox,{css:({ ["position"] : "relative", ["width"] : "25%", ["minHeight"] : "120px", ["paddingTop"] : "0" }),key:index_88bde4c6288affda480f97a1eded32d0},jsx(Fragment,{},(!((item_rx_state_?.["id"]?.valueOf?.() === "3"?.valueOf?.()))?(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["position"] : "absolute", ["top"] : "5px", ["left"] : "calc(50% + 10px)", ["width"] : "calc(100% - 20px)", ["height"] : "3px", ["background"] : ((item_rx_state_?.["line_after"]?.valueOf?.() === "done"?.valueOf?.()) ? "#d92314" : "#e5e7eb"), ["borderRadius"] : "999px", ["zIndex"] : "1" })},))):(jsx(Fragment,{},)))),jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"2"},jsx(RadixThemesBox,{css:({ ["width"] : "12px", ["height"] : "12px", ["borderRadius"] : "999px", ["background"] : ((item_rx_state_?.["state"]?.valueOf?.() === "upcoming"?.valueOf?.()) ? "#bdbdbd" : "#d92314"), ["boxShadow"] : "0 0 0 4px white", ["zIndex"] : "2" })},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "11px", ["fontWeight"] : "700", ["color"] : ((item_rx_state_?.["state"]?.valueOf?.() === "upcoming"?.valueOf?.()) ? "#8a8a8a" : "#1f2937") })},item_rx_state_?.["start"]),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "11px", ["fontWeight"] : "700", ["color"] : ((item_rx_state_?.["state"]?.valueOf?.() === "upcoming"?.valueOf?.()) ? "#8a8a8a" : "#1f2937") })},item_rx_state_?.["end"]),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "11px", ["color"] : ((item_rx_state_?.["state"]?.valueOf?.() === "upcoming"?.valueOf?.()) ? "#8a8a8a" : "#1f2937"), ["textAlign"] : "center", ["lineHeight"] : "1.5" })},item_rx_state_?.["label"])))))))
  )
}


function Text_e8dd8a503c9968000318f056a501d954 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["fontWeight"] : "700", ["color"] : "#1d4ed8" })},reflex___state____state__ptit_reflex___state____conduct_state.selected_semester_name_rx_state_)
  )
}


function Text_4229b68ecc92bad8ebd8291d5c9ae0bb () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : "white", ["fontSize"] : "13px", ["fontWeight"] : "700" })},reflex___state____state__ptit_reflex___state____conduct_state.score_effective_total_rx_state_)
  )
}


function Text_7869b5e64eb2b8b79ef0f76667f5f3ca () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["fontWeight"] : "700", ["color"] : "#0369a1" })},reflex___state____state__ptit_reflex___state____conduct_state.conduct_grade_label_rx_state_)
  )
}


function Select__root_8935d99c6f10dd01dcc58649f26210f1 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_fc43cac6d9a225b19126d3c9e8dbcee6 = useCallback(((_ev_0) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.select_semester_by_name", ({ ["name"] : _ev_0 }), ({  })))], [_ev_0], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesSelect.Root,{css:({ ["minWidth"] : "240px", ["maxWidth"] : "280px", ["height"] : "40px", ["border"] : "1px solid #d92314", ["borderRadius"] : "10px", ["background"] : "white", ["color"] : "#1f2937", ["fontSize"] : "14px", ["fontWeight"] : "500", ["paddingLeft"] : "12px", ["paddingRight"] : "12px" }),onValueChange:on_change_fc43cac6d9a225b19126d3c9e8dbcee6,value:reflex___state____state__ptit_reflex___state____conduct_state.selected_semester_name_rx_state_},jsx(RadixThemesSelect.Trigger,{css:({ ["width"] : "280px" })},),jsx(RadixThemesSelect.Content,{},jsx(Select__group_91fe2be0f0af2134f6d6b2335837614e,{},)))
  )
}


function Text_fbb83647339ac271152c088efc7c46aa () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},reflex___state____state__ptit_reflex___state____conduct_state.submission_status_label_rx_state_)
  )
}


function Fragment_11fcaee6bdcdedc542f08f1ddcf657d9 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.outside_window_rx_state_?(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["padding"] : "6px 12px", ["borderRadius"] : "999px", ["background"] : "#d92314" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["fontWeight"] : "700", ["color"] : "white" })},"Ngo\u00e0i th\u1eddi gian ch\u1ea5m \u0111i\u1ec3m")))):(jsx(Fragment,{},))))
  )
}


function Text_f99260fafe288f8a5b7f5656a2427156 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},reflex___state____state__ptit_reflex___state____conduct_state.score_total_rx_state_)
  )
}


function Text_ace28a78b06011ccbbd9c6afaafe9e7d () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},reflex___state____state__ptit_reflex___state____conduct_state.score_total_class_rx_state_)
  )
}


function Text_593b95e94b1675df44282458b1cbe821 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},reflex___state____state__ptit_reflex___state____conduct_state.score_total_advisor_rx_state_)
  )
}


function Fragment_d9a4149fd1c29071c6c220880652e1d3 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},((reflex___state____state__ptit_reflex___state____conduct_state.submission_status_rx_state_?.valueOf?.() === "student_submitted"?.valueOf?.())?(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "12px 16px", ["textAlign"] : "center", ["borderTop"] : "1px solid #e5e7eb", ["background"] : "#f0fdf4" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["fontWeight"] : "600", ["color"] : "#15803d" })},"\u0110\u00e3 g\u1eedi \u0111\u00e1nh gi\u00e1")))):(jsx(Fragment,{},))))
  )
}


function Box_ae8b07dbb9e6e6345c70b0526abd29a1 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    jsx(RadixThemesBox,{css:({ ["minWidth"] : "900px", ["width"] : "100%", ["background"] : "white" })},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%", ["background"] : "#f8fafc" }),direction:"row",gap:"0"},jsx(RadixThemesBox,{css:({ ["width"] : "auto", ["flex"] : (true ? "1" : "none"), ["padding"] : "14px 10px", ["borderRight"] : "1px solid #e5e7eb", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["fontWeight"] : "700", ["color"] : "#374151", ["textAlign"] : "center" })},"N\u1ed8I DUNG")),jsx(RadixThemesBox,{css:({ ["width"] : "120px", ["flex"] : (false ? "1" : "none"), ["padding"] : "14px 10px", ["borderRight"] : "1px solid #e5e7eb", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["fontWeight"] : "700", ["color"] : "#374151", ["textAlign"] : "center" })},"\u0110i\u1ec3m t\u1ed1i \u0111a")),jsx(RadixThemesBox,{css:({ ["width"] : "160px", ["flex"] : (false ? "1" : "none"), ["padding"] : "14px 10px", ["borderRight"] : "1px solid #e5e7eb", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["fontWeight"] : "700", ["color"] : "#374151", ["textAlign"] : "center" })},"Sinh vi\u00ean")),jsx(RadixThemesBox,{css:({ ["width"] : "160px", ["flex"] : (false ? "1" : "none"), ["padding"] : "14px 10px", ["borderRight"] : "1px solid #e5e7eb", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["fontWeight"] : "700", ["color"] : "#374151", ["textAlign"] : "center" })},"Duy\u1ec7t")),jsx(RadixThemesBox,{css:({ ["width"] : "160px", ["flex"] : (false ? "1" : "none"), ["padding"] : "14px 10px", ["borderRight"] : "1px solid #e5e7eb", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["fontWeight"] : "700", ["color"] : "#374151", ["textAlign"] : "center" })},"CVHT"))),Array.prototype.map.call(reflex___state____state__ptit_reflex___state____conduct_state.score_rows_rx_state_ ?? [],((row_rx_state_,index_b84d414bded936bb5574c7134590e6c8)=>(jsx(Fragment,{key:index_b84d414bded936bb5574c7134590e6c8},((row_rx_state_?.["kind"]?.valueOf?.() === "group"?.valueOf?.())?(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%", ["borderTop"] : "1px solid #e5e7eb", ["background"] : "white" }),direction:"row",gap:"0"},jsx(RadixThemesBox,{css:({ ["flex"] : "1", ["padding"] : "14px 16px" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["fontWeight"] : "600", ["color"] : "#1f2937", ["lineHeight"] : "1.6" })},row_rx_state_?.["title"])),jsx(RadixThemesBox,{css:({ ["width"] : "120px", ["padding"] : "14px 10px", ["textAlign"] : "center" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["fontWeight"] : "600", ["color"] : "#1f2937" })},row_rx_state_?.["max_points"])),jsx(RadixThemesBox,{css:({ ["width"] : "160px" })},),jsx(RadixThemesBox,{css:({ ["width"] : "160px" })},),jsx(RadixThemesBox,{css:({ ["width"] : "160px" })},)))):(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["borderTop"] : "1px solid #e5e7eb", ["background"] : "white" }),direction:"row",gap:"0"},jsx(RadixThemesBox,{css:({ ["flex"] : "1", ["minWidth"] : "200px", ["padding"] : "14px 12px" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["color"] : "#374151", ["lineHeight"] : "1.6", ["overflowWrap"] : "anywhere" })},row_rx_state_?.["title"])),jsx(RadixThemesBox,{css:({ ["width"] : "120px", ["padding"] : "14px 10px", ["textAlign"] : "center" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["color"] : "#6b7280" })},row_rx_state_?.["range"])),jsx(RadixThemesBox,{css:({ ["width"] : "160px", ["padding"] : "10px 12px", ["display"] : "flex", ["justifyContent"] : "center" })},jsx(Fragment,{},(isTrue(row_rx_state_?.["self_editable"])?(jsx(Fragment,{},jsx(RadixThemesTextField.Root,{css:({ ["width"] : "100px", ["height"] : "38px", ["textAlign"] : "center", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "6px", ["background"] : "white" }),defaultValue:row_rx_state_?.["self_score"],key:("self_score-"+row_rx_state_?.["criterion_id"]+"-"+reflex___state____state__ptit_reflex___state____conduct_state.selected_student_id_rx_state_+"-"+reflex___state____state__ptit_reflex___state____conduct_state.selected_semester_id_rx_state_),max:row_rx_state_?.["max_points_value"],min:row_rx_state_?.["min_points"],onChange:((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.update_score", ({ ["criterion_id"] : row_rx_state_?.["criterion_id"], ["field_name"] : "self_score", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))),onInput:
        (e) => {
            const raw = e.target.value;
            if (raw === "" || raw === null || raw === undefined) {
                return;
            }
            const parsed = Number(raw);
            if (Number.isNaN(parsed)) {
                return;
            }
            const min = Number(e.target.min);
            const max = Number(e.target.max);
            let clamped = parsed;
            if (!Number.isNaN(max) && clamped > max) {
                clamped = max;
            }
            if (!Number.isNaN(min) && clamped < min) {
                clamped = min;
            }
            if (clamped !== parsed) {
                e.target.value = Number.isInteger(clamped) ? String(Math.trunc(clamped)) : String(clamped);
            }
        }
        ,step:"0.01",type:"number"},))):(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["width"] : "100px", ["height"] : "38px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "6px", ["background"] : "#f8fafc", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["color"] : ((row_rx_state_?.["self_score"]?.valueOf?.() === ""?.valueOf?.()) ? "#c7c7c7" : "#6b7280") })},row_rx_state_?.["self_score"]))))))),jsx(RadixThemesBox,{css:({ ["width"] : "160px", ["padding"] : "10px 12px", ["display"] : "flex", ["justifyContent"] : "center" })},jsx(Fragment,{},(isTrue(row_rx_state_?.["class_editable"])?(jsx(Fragment,{},jsx(RadixThemesTextField.Root,{css:({ ["width"] : "100px", ["height"] : "38px", ["textAlign"] : "center", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "6px", ["background"] : "white" }),defaultValue:row_rx_state_?.["class_score"],key:("class_score-"+row_rx_state_?.["criterion_id"]+"-"+reflex___state____state__ptit_reflex___state____conduct_state.selected_student_id_rx_state_+"-"+reflex___state____state__ptit_reflex___state____conduct_state.selected_semester_id_rx_state_),max:row_rx_state_?.["max_points_value"],min:row_rx_state_?.["min_points"],onChange:((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.update_score", ({ ["criterion_id"] : row_rx_state_?.["criterion_id"], ["field_name"] : "class_score", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))),onInput:
        (e) => {
            const raw = e.target.value;
            if (raw === "" || raw === null || raw === undefined) {
                return;
            }
            const parsed = Number(raw);
            if (Number.isNaN(parsed)) {
                return;
            }
            const min = Number(e.target.min);
            const max = Number(e.target.max);
            let clamped = parsed;
            if (!Number.isNaN(max) && clamped > max) {
                clamped = max;
            }
            if (!Number.isNaN(min) && clamped < min) {
                clamped = min;
            }
            if (clamped !== parsed) {
                e.target.value = Number.isInteger(clamped) ? String(Math.trunc(clamped)) : String(clamped);
            }
        }
        ,step:"0.01",type:"number"},))):(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["width"] : "100px", ["height"] : "38px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "6px", ["background"] : "#f8fafc", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["color"] : ((row_rx_state_?.["class_score"]?.valueOf?.() === ""?.valueOf?.()) ? "#c7c7c7" : "#6b7280") })},row_rx_state_?.["class_score"]))))))),jsx(RadixThemesBox,{css:({ ["width"] : "160px", ["padding"] : "10px 12px", ["display"] : "flex", ["justifyContent"] : "center" })},jsx(Fragment,{},(isTrue(row_rx_state_?.["advisor_editable"])?(jsx(Fragment,{},jsx(RadixThemesTextField.Root,{css:({ ["width"] : "100px", ["height"] : "38px", ["textAlign"] : "center", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "6px", ["background"] : "white" }),defaultValue:row_rx_state_?.["advisor_score"],key:("advisor_score-"+row_rx_state_?.["criterion_id"]+"-"+reflex___state____state__ptit_reflex___state____conduct_state.selected_student_id_rx_state_+"-"+reflex___state____state__ptit_reflex___state____conduct_state.selected_semester_id_rx_state_),max:row_rx_state_?.["max_points_value"],min:row_rx_state_?.["min_points"],onChange:((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.update_score", ({ ["criterion_id"] : row_rx_state_?.["criterion_id"], ["field_name"] : "advisor_score", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))),onInput:
        (e) => {
            const raw = e.target.value;
            if (raw === "" || raw === null || raw === undefined) {
                return;
            }
            const parsed = Number(raw);
            if (Number.isNaN(parsed)) {
                return;
            }
            const min = Number(e.target.min);
            const max = Number(e.target.max);
            let clamped = parsed;
            if (!Number.isNaN(max) && clamped > max) {
                clamped = max;
            }
            if (!Number.isNaN(min) && clamped < min) {
                clamped = min;
            }
            if (clamped !== parsed) {
                e.target.value = Number.isInteger(clamped) ? String(Math.trunc(clamped)) : String(clamped);
            }
        }
        ,step:"0.01",type:"number"},))):(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["width"] : "100px", ["height"] : "38px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "6px", ["background"] : "#f8fafc", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["color"] : ((row_rx_state_?.["advisor_score"]?.valueOf?.() === ""?.valueOf?.()) ? "#c7c7c7" : "#6b7280") })},row_rx_state_?.["advisor_score"]))))))))))))))),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%", ["borderTop"] : "1px solid #e5e7eb", ["background"] : "#f9fafb" }),direction:"row",gap:"0"},jsx(RadixThemesBox,{css:({ ["flex"] : "1", ["padding"] : "16px" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "16px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},"T\u1ed4NG \u0110I\u1ec2M")),jsx(RadixThemesBox,{css:({ ["width"] : "120px", ["padding"] : "16px 10px", ["textAlign"] : "center" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},"100")),jsx(RadixThemesBox,{css:({ ["width"] : "160px", ["padding"] : "16px 10px", ["textAlign"] : "center" })},jsx(Text_f99260fafe288f8a5b7f5656a2427156,{},)),jsx(RadixThemesBox,{css:({ ["width"] : "160px", ["padding"] : "16px 10px", ["textAlign"] : "center" })},jsx(Text_ace28a78b06011ccbbd9c6afaafe9e7d,{},)),jsx(RadixThemesBox,{css:({ ["width"] : "160px", ["padding"] : "16px 10px", ["textAlign"] : "center" })},jsx(Text_593b95e94b1675df44282458b1cbe821,{},))),jsx(Fragment_d9a4149fd1c29071c6c220880652e1d3,{},))
  )
}


function Button_e89927dd4321f7f46cf92e7a13d24fd8 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_4682dccc5900b7912f56bf99380f85eb = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.save_student_draft", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : "white", ["color"] : "#1f2937", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:on_click_4682dccc5900b7912f56bf99380f85eb},"L\u01b0u t\u1ea1m")
  )
}


function Fragment_760b97a0a33b9dc720236bbd2af0884a () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.can_save_student_rx_state_?(jsx(Fragment,{},jsx(Button_e89927dd4321f7f46cf92e7a13d24fd8,{},))):(jsx(Fragment,{},))))
  )
}


function Button_759ccf080f219146f1b01adad3a097f3 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_1975eeb17411ad2dae7ad570ead441a4 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.save_class_scores", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : "white", ["color"] : "#1f2937", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:on_click_1975eeb17411ad2dae7ad570ead441a4},"L\u01b0u phi\u1ebfu")
  )
}


function Fragment_0eb58ee5291243e13fc6f87c021270f0 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.can_save_class_rx_state_?(jsx(Fragment,{},jsx(Button_759ccf080f219146f1b01adad3a097f3,{},))):(jsx(Fragment,{},))))
  )
}


function Button_73b234a0d6c5078bac641d1ecd2b874f () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_8ffdcaecd3daa8000d925114fb216116 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.submit_student_scores", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : "#d92314", ["color"] : "white", ["border"] : "none", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:on_click_8ffdcaecd3daa8000d925114fb216116},"G\u1eedi \u0111\u00e1nh gi\u00e1")
  )
}


function Fragment_a297e8428f94046be07fe5968b8472ef () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.can_submit_student_rx_state_?(jsx(Fragment,{},jsx(Button_73b234a0d6c5078bac641d1ecd2b874f,{},))):(jsx(Fragment,{},))))
  )
}


function Button_1d8b8e03d0a31fbfae2267502bde1fbd () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_54d49caef9520009ccecd5135a604c03 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.approve_class_scores", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : "#b91c1c", ["color"] : "white", ["border"] : "none", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:on_click_54d49caef9520009ccecd5135a604c03},"Duy\u1ec7t")
  )
}


function Fragment_07b417834776fcdd531fd0795e3c68a3 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.can_review_class_rx_state_?(jsx(Fragment,{},jsx(Button_1d8b8e03d0a31fbfae2267502bde1fbd,{},))):(jsx(Fragment,{},))))
  )
}


function Button_896c7535c45a19559bbb8e184882564e () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_4fa8a954c41bcbbbf71637e745ca9577 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.approve_advisor_scores", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : "#15803d", ["color"] : "white", ["border"] : "none", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:on_click_4fa8a954c41bcbbbf71637e745ca9577},"X\u00e1c nh\u1eadn")
  )
}


function Fragment_b46cd2c128f09c84d3b7995be966d930 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.can_review_advisor_rx_state_?(jsx(Fragment,{},jsx(Button_896c7535c45a19559bbb8e184882564e,{},))):(jsx(Fragment,{},))))
  )
}


function Button_40bdc07d9fbd1da5335c229e1037cc79 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_3e598de6d387a37251c9968ba93e9729 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.download_conduct_pdf", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : "white", ["color"] : "#1f2937", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:on_click_3e598de6d387a37251c9968ba93e9729},"T\u1ea3i PDF")
  )
}


function Fragment_832a7b5be861cffd0baca88f9c731e68 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.can_download_conduct_pdf_rx_state_?(jsx(Fragment,{},jsx(Button_40bdc07d9fbd1da5335c229e1037cc79,{},))):(jsx(Fragment,{},))))
  )
}


function Button_ef4290285b82a12c27ebf5ad3c2fe22c () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_f1f674936fdd7eda80fbcefc74e884b6 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.reset_submission", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : "#fff1f2", ["color"] : "#d92314", ["border"] : "1px solid #fecdd3", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:on_click_f1f674936fdd7eda80fbcefc74e884b6},"\u0110\u1eb7t l\u1ea1i")
  )
}


function Fragment_cafb9321feb0633a58d829342881884d () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.can_reset_submission_rx_state_?(jsx(Fragment,{},jsx(Button_ef4290285b82a12c27ebf5ad3c2fe22c,{},))):(jsx(Fragment,{},))))
  )
}


function Fragment_3f518e591fba453eccfd8c5567f34208 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_score"?.valueOf?.())?(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%", ["minWidth"] : "0" }),direction:"column",gap:"4"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "22px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},"Phi\u1ebfu \u0111i\u1ec3m r\u00e8n luy\u1ec7n"),jsx(Fragment_4825087903813d4c4fdeb030523e3f8e,{},),jsx(RadixThemesBox,{css:({ ["background"] : "white", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "12px", ["width"] : "100%", ["maxWidth"] : "100%", ["minWidth"] : "0", ["padding"] : "20px" })},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%", ["minHeight"] : "0" }),direction:"column",gap:"4"},jsx(Flex_6d27a14838fa9b4ecd4b33e914d5c3da,{},),jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["flex"] : "1", ["minHeight"] : "0", ["display"] : "flex", ["flexDirection"] : "column", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "10px", ["overflow"] : "hidden", ["background"] : "white" })},jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["background"] : "white" })},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["minHeight"] : "52px", ["padding"] : "8px 12px", ["flexWrap"] : "wrap", ["borderBottom"] : "1px solid #e5e7eb", ["background"] : "white" }),direction:"row",justify:"between",gap:"3"},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["flexWrap"] : "wrap" }),direction:"row",gap:"3"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "16px", ["fontWeight"] : "800", ["color"] : "#1f2937" })},"PHI\u1ebeU \u0110I\u1ec2M R\u00c8N LUY\u1ec6N"),jsx(RadixThemesBox,{css:({ ["padding"] : "6px 12px", ["borderRadius"] : "999px", ["background"] : "#eff6ff" })},jsx(Text_e8dd8a503c9968000318f056a501d954,{},)),jsx(RadixThemesBox,{css:({ ["background"] : "#d92314", ["borderRadius"] : "8px", ["padding"] : "6px 12px" })},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",direction:"row",gap:"1"},jsx(Text_4229b68ecc92bad8ebd8291d5c9ae0bb,{},),jsx(RadixThemesText,{as:"p",css:({ ["color"] : "white", ["fontSize"] : "13px", ["fontWeight"] : "700" })},"\u0111i\u1ec3m"))),jsx(RadixThemesBox,{css:({ ["padding"] : "6px 12px", ["borderRadius"] : "999px", ["background"] : "#e0f2fe" })},jsx(Text_7869b5e64eb2b8b79ef0f76667f5f3ca,{},))),jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["flexWrap"] : "wrap" }),direction:"row",gap:"3"},jsx(Select__root_8935d99c6f10dd01dcc58649f26210f1,{},),jsx(RadixThemesBox,{css:({ ["padding"] : "6px 12px", ["borderRadius"] : "999px", ["background"] : "#e5e7eb" })},jsx(Text_fbb83647339ac271152c088efc7c46aa,{},)),jsx(Fragment_11fcaee6bdcdedc542f08f1ddcf657d9,{},)))),jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["flex"] : "1", ["minHeight"] : "0", ["padding"] : "12px 16px 16px", ["display"] : "flex", ["flexDirection"] : "column" })},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%", ["minWidth"] : "0", ["flex"] : "1" }),direction:"column",gap:"4"},jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["maxWidth"] : "100%", ["overflowX"] : "auto", ["overflowY"] : "hidden", ["flex"] : "1", ["minHeight"] : "0", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" })},jsx(Box_ae8b07dbb9e6e6345c70b0526abd29a1,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%", ["flexWrap"] : "wrap" }),direction:"row",justify:"end",gap:"3"},jsx(Fragment_760b97a0a33b9dc720236bbd2af0884a,{},),jsx(Fragment_0eb58ee5291243e13fc6f87c021270f0,{},),jsx(Fragment_a297e8428f94046be07fe5968b8472ef,{},),jsx(Fragment_07b417834776fcdd531fd0795e3c68a3,{},),jsx(Fragment_b46cd2c128f09c84d3b7995be966d930,{},),jsx(Fragment_832a7b5be861cffd0baca88f9c731e68,{},),jsx(Fragment_cafb9321feb0633a58d829342881884d,{},)))))))))):(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%", ["minWidth"] : "0" }),direction:"column",gap:"4"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "22px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},"Phi\u1ebfu \u0111i\u1ec3m r\u00e8n luy\u1ec7n"),jsx(Fragment_4825087903813d4c4fdeb030523e3f8e,{},),jsx(RadixThemesBox,{css:({ ["background"] : "white", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "12px", ["width"] : "100%", ["maxWidth"] : "100%", ["minWidth"] : "0", ["padding"] : "20px" })},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%", ["minHeight"] : "0" }),direction:"column",gap:"4"},jsx(Flex_6d27a14838fa9b4ecd4b33e914d5c3da,{},),jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["flex"] : "1", ["minHeight"] : "0", ["display"] : "flex", ["flexDirection"] : "column", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "10px", ["overflow"] : "hidden", ["background"] : "white" })},jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["background"] : "white" })},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["minHeight"] : "52px", ["padding"] : "8px 12px", ["flexWrap"] : "wrap", ["borderBottom"] : "1px solid #e5e7eb", ["background"] : "white" }),direction:"row",justify:"between",gap:"3"},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["flexWrap"] : "wrap" }),direction:"row",gap:"3"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "16px", ["fontWeight"] : "800", ["color"] : "#1f2937" })},"PHI\u1ebeU \u0110I\u1ec2M R\u00c8N LUY\u1ec6N"),jsx(RadixThemesBox,{css:({ ["padding"] : "6px 12px", ["borderRadius"] : "999px", ["background"] : "#eff6ff" })},jsx(Text_e8dd8a503c9968000318f056a501d954,{},)),jsx(RadixThemesBox,{css:({ ["background"] : "#d92314", ["borderRadius"] : "8px", ["padding"] : "6px 12px" })},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",direction:"row",gap:"1"},jsx(Text_4229b68ecc92bad8ebd8291d5c9ae0bb,{},),jsx(RadixThemesText,{as:"p",css:({ ["color"] : "white", ["fontSize"] : "13px", ["fontWeight"] : "700" })},"\u0111i\u1ec3m"))),jsx(RadixThemesBox,{css:({ ["padding"] : "6px 12px", ["borderRadius"] : "999px", ["background"] : "#e0f2fe" })},jsx(Text_7869b5e64eb2b8b79ef0f76667f5f3ca,{},))),jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["flexWrap"] : "wrap" }),direction:"row",gap:"3"},jsx(Select__root_8935d99c6f10dd01dcc58649f26210f1,{},),jsx(RadixThemesBox,{css:({ ["padding"] : "6px 12px", ["borderRadius"] : "999px", ["background"] : "#e5e7eb" })},jsx(Text_fbb83647339ac271152c088efc7c46aa,{},)),jsx(Fragment_11fcaee6bdcdedc542f08f1ddcf657d9,{},)))),jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["flex"] : "1", ["minHeight"] : "0", ["padding"] : "12px 16px 16px", ["display"] : "flex", ["flexDirection"] : "column" })},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%", ["minWidth"] : "0", ["flex"] : "1" }),direction:"column",gap:"4"},jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["maxWidth"] : "100%", ["overflowX"] : "auto", ["overflowY"] : "hidden", ["flex"] : "1", ["minHeight"] : "0", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" })},jsx(Box_ae8b07dbb9e6e6345c70b0526abd29a1,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%", ["flexWrap"] : "wrap" }),direction:"row",justify:"end",gap:"3"},jsx(Fragment_760b97a0a33b9dc720236bbd2af0884a,{},),jsx(Fragment_0eb58ee5291243e13fc6f87c021270f0,{},),jsx(Fragment_a297e8428f94046be07fe5968b8472ef,{},),jsx(Fragment_07b417834776fcdd531fd0795e3c68a3,{},),jsx(Fragment_b46cd2c128f09c84d3b7995be966d930,{},),jsx(Fragment_832a7b5be861cffd0baca88f9c731e68,{},),jsx(Fragment_cafb9321feb0633a58d829342881884d,{},))))))))))))
  )
}


function Fragment_3a6113ee9c4e20343de8969dfb8b72e0 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_evidence"?.valueOf?.())?(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"4"},jsx(Fragment_265f21a195b0dc4dc19ed007f2fd2f39,{},),jsx(Fragment_4825087903813d4c4fdeb030523e3f8e,{},),jsx(RadixThemesBox,{css:({ ["background"] : "white", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "12px", ["width"] : "100%", ["overflow"] : "hidden", ["position"] : "relative" })},jsx(RadixThemesBox,{css:({ ["padding"] : "16px 18px", ["borderBottom"] : "1px solid #e5e7eb" })},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["flexWrap"] : "wrap" }),direction:"row",justify:"between",gap:"3"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"column",gap:"0"},jsx(Fragment_e481484b0e70c316b06b1f0a2afbbf4c,{},),jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["flexWrap"] : "wrap" }),direction:"row",gap:"2"},jsx(Text_8e2de377a3aac2e9e3e7ac3f4b525aab,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["color"] : "#6b7280" })},"\u2022"),jsx(Text_77e76f365172eccc54e58040eda12034,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["color"] : "#6b7280" })},"\u2022"),jsx(Text_84db5c447968c18c7a5993ff3bc1a4f8,{},))),jsx(Fragment_0b630256d90782375a7752fe4bfe5e58,{},))),jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%", ["minWidth"] : "0" }),direction:"row",gap:"0"},jsx(Box_8696ab88fa1fc9db2a0dbada4e4c99a9,{},),jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%", ["padding"] : "16px", ["position"] : "relative", ["minWidth"] : "0" }),direction:"column",gap:"4"},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["flexWrap"] : "wrap" }),direction:"row",justify:"between",gap:"3"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "18px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},"Danh s\u00e1ch minh ch\u1ee9ng"),jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",direction:"row",gap:"3"},jsx(Fragment_ea1e6bff2d6db7a16f88816696e81df9,{},),jsx(Button_c4b809ba8276fba3517b115a4827a629,{},),jsx(RadixThemesBox,{css:({ ["display"] : "flex", ["alignItems"] : "center", ["gap"] : "4px", ["padding"] : "0 14px", ["height"] : "38px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" })},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#6b7280" })},"T\u1ed5ng s\u1ed1: "),jsx(Text_eb35ab60d861402244d1ec721be75434,{},)),jsx(RadixThemesBox,{css:({ ["position"] : "relative" })},jsx(Button_9d89a725a5df0988bd04431cb0857f95,{},)))),jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["overflowX"] : "auto", ["overflowY"] : "hidden", ["position"] : "relative" })},jsx(RadixThemesBox,{css:({ ["minWidth"] : "1164px", ["width"] : "100%" })},jsx(Box_17d55afa5f7e1a7ea055327efc5179b4,{},),jsx(Fragment_3105c8464f9695214961f79be329256c,{},)))))),jsx(Fragment_f846582f20ef649825a1dafacbb945d6,{},)))):(jsx(Fragment_3f518e591fba453eccfd8c5567f34208,{},))))
  )
}


function Fragment_e20dd0a627ce8e95a3a88a8b78fcf327 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_events"?.valueOf?.())?(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"4"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "22px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},"Duy\u1ec7t s\u1ef1 ki\u1ec7n \u0111\u00e3 \u0111\u0103ng k\u00fd"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["color"] : "#6b7280", ["lineHeight"] : "1.7" })},"M\u00e0n n\u00e0y ch\u1ec9 hi\u1ec3n th\u1ecb c\u00e1c s\u1ef1 ki\u1ec7n sinh vi\u00ean \u0111\u00e3 \u0111\u0103ng k\u00fd \u0111\u1ec3 ban c\u00e1n s\u1ef1 duy\u1ec7t, kh\u00f4ng hi\u1ec3n th\u1ecb ph\u1ea7n \u0111\u0103ng k\u00fd s\u1ef1 ki\u1ec7n m\u1edbi."),jsx(RadixThemesBox,{css:({ ["background"] : "white", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "12px", ["width"] : "100%", ["padding"] : "24px" })},jsx(Fragment_84eda3506f28e66b6de13fda6a2ae187,{},))))):(jsx(Fragment_3a6113ee9c4e20343de8969dfb8b72e0,{},))))
  )
}


function Fragment_ed59db8d2c900253d76e1b6bcfc2d97e () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_events_list"?.valueOf?.())?(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"4"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "22px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},"Duy\u1ec7t s\u1ef1 ki\u1ec7n"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["color"] : "#6b7280" })},"Ch\u1ecdn t\u1eebng sinh vi\u00ean \u0111\u1ec3 m\u1edf danh s\u00e1ch s\u1ef1 ki\u1ec7n \u0111\u00e3 \u0111\u0103ng k\u00fd v\u00e0 duy\u1ec7t c\u00e1c \u0111\u0103ng k\u00fd \u0111ang ch\u1edd x\u1eed l\u00fd."),jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["flexWrap"] : "wrap" }),direction:"row",justify:"between",gap:"3"},jsx(RadixThemesBox,{css:({ ["flex"] : "1", ["minWidth"] : "280px" })},jsx(Debounceinput_214c1d76a9e3c638f421e3e87eccf285,{},)),jsx(Select__root_ee6018cea39361f01aceb82959ee1920,{},)),jsx(Flex_757262c88f28240466c44c37c9372c98,{},)))):(jsx(Fragment_e20dd0a627ce8e95a3a88a8b78fcf327,{},))))
  )
}


function Fragment_81840a97c163f12a251247ba40294a62 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_evidence_list"?.valueOf?.())?(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"4"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "22px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},"Duy\u1ec7t minh ch\u1ee9ng"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["color"] : "#6b7280" })},"Ch\u1ecdn t\u1eebng sinh vi\u00ean \u0111\u1ec3 m\u1edf l\u1ea1i m\u00e0n h\u00ecnh duy\u1ec7t minh ch\u1ee9ng hi\u1ec7n c\u00f3. Danh s\u00e1ch v\u1eabn hi\u1ec3n th\u1ecb s\u1ed1 minh ch\u1ee9ng \u0111ang ch\u1edd ban c\u00e1n s\u1ef1 x\u1eed l\u00fd."),jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["flexWrap"] : "wrap" }),direction:"row",justify:"between",gap:"3"},jsx(RadixThemesBox,{css:({ ["flex"] : "1", ["minWidth"] : "280px" })},jsx(Debounceinput_214c1d76a9e3c638f421e3e87eccf285,{},)),jsx(Select__root_ee6018cea39361f01aceb82959ee1920,{},)),jsx(Flex_86f572b2e186b8a68a05d61b4609d792,{},)))):(jsx(Fragment_ed59db8d2c900253d76e1b6bcfc2d97e,{},))))
  )
}


function Fragment_d145f9f04bdaa2f6f9d379dee548f3d2 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students_score_list"?.valueOf?.())?(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"4"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "22px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},"Duy\u1ec7t phi\u1ebfu \u0111i\u1ec3m r\u00e8n luy\u1ec7n"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["color"] : "#6b7280" })},"Danh s\u00e1ch d\u01b0\u1edbi \u0111\u00e2y d\u00e0nh cho ban c\u00e1n s\u1ef1. M\u1edf phi\u1ebfu \u0111\u1ec3 xem, ch\u1ec9nh \u0111i\u1ec3m v\u00e0 ch\u1ec9 duy\u1ec7t trong m\u00e0n phi\u1ebfu khi \u0111\u00fang th\u1eddi gian ban c\u00e1n s\u1ef1 \u0111\u00e1nh gi\u00e1."),jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["flexWrap"] : "wrap" }),direction:"row",justify:"between",gap:"3"},jsx(RadixThemesBox,{css:({ ["flex"] : "1", ["minWidth"] : "280px" })},jsx(Debounceinput_214c1d76a9e3c638f421e3e87eccf285,{},)),jsx(Select__root_ee6018cea39361f01aceb82959ee1920,{},)),jsx(Flex_314aef5b530c1551124c602e2b17f867,{},)))):(jsx(Fragment_81840a97c163f12a251247ba40294a62,{},))))
  )
}


function Fragment_293d9760423a245231825532a6975074 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "students"?.valueOf?.())?(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"4"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "22px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},"Danh s\u00e1ch sinh vi\u00ean"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["color"] : "#6b7280" })},"Nh\u1ea5n v\u00e0o t\u00ean sinh vi\u00ean \u0111\u1ec3 xem th\u00f4ng tin chi ti\u1ebft; d\u00f9ng n\u00fat b\u00ean ph\u1ea3i \u0111\u1ec3 m\u1edf phi\u1ebfu \u0111i\u1ec3m r\u00e8n luy\u1ec7n."),jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["flexWrap"] : "wrap" }),direction:"row",justify:"between",gap:"3"},jsx(RadixThemesBox,{css:({ ["flex"] : "1", ["minWidth"] : "280px" })},jsx(Debounceinput_214c1d76a9e3c638f421e3e87eccf285,{},)),jsx(Select__root_ee6018cea39361f01aceb82959ee1920,{},)),jsx(Flex_cc6906835f6e8ffb286333af349ae142,{},)))):(jsx(Fragment_d145f9f04bdaa2f6f9d379dee548f3d2,{},))))
  )
}


function Fragment_880553d749dd4dd1be3fa071760e6064 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "admin_events"?.valueOf?.())?(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"4"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "22px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},"T\u1ea1o s\u1ef1 ki\u1ec7n"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["color"] : "#6b7280" })},"Ch\u1ec9 t\u1ea1o c\u00e1c s\u1ef1 ki\u1ec7n t\u1ef1 \u0111\u1ed9ng t\u00ednh \u0111i\u1ec3m r\u00e8n luy\u1ec7n trong h\u1ecdc k\u1ef3 \u0111\u00e3 ch\u1ecdn. Sinh vi\u00ean ch\u1ec9 \u0111\u0103ng k\u00fd \u0111\u01b0\u1ee3c trong h\u1ecdc k\u1ef3 \u0111ang ho\u1ea1t \u0111\u1ed9ng v\u00e0 \u0111i\u1ec3m ch\u1ec9 c\u1ed9ng cho \u0111\u00fang h\u1ecdc k\u1ef3 c\u1ee7a s\u1ef1 ki\u1ec7n \u0111\u00f3."),jsx(RadixThemesBox,{css:({ ["background"] : "white", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "12px", ["padding"] : "24px", ["width"] : "100%" })},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%", ["maxWidth"] : "560px" }),direction:"column",gap:"4"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* H\u1ecdc k\u1ef3"),jsx(Select__root_75a33be3164c7fddda54a3c0dee52d8b,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* Ti\u00eau ch\u00ed c\u1ed9ng \u0111i\u1ec3m"),jsx(Select__root_27665ec93a769bfc897f18c6a00ab102,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* T\u00ean s\u1ef1 ki\u1ec7n"),jsx(Debounceinput_f9585af75e7df0e7d2f9ac5c50ed3e65,{},),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%", ["flexWrap"] : "wrap" }),direction:"row",gap:"4"},jsx(RadixThemesBox,{css:({ ["width"] : "100%" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* Th\u1eddi gian b\u1eaft \u0111\u1ea7u"),jsx(Debounceinput_a8f0e3a5c61216540f9615a06dfd95a3,{},)),jsx(RadixThemesBox,{css:({ ["width"] : "100%" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* Th\u1eddi gian k\u1ebft th\u00fac"),jsx(Debounceinput_d3273f05204672b3e8579c0989b39491,{},))),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* \u0110\u1ecba \u0111i\u1ec3m"),jsx(Debounceinput_eb4c4f95bbf80b01aaae4a92bd2df201,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* \u0110i\u1ec3m t\u1ed1i \u0111a"),jsx(Debounceinput_5711941a38c137cc50aea192e5507487,{},),jsx(RadixThemesBox,{css:({ ["width"] : "200px" })},jsx(Button_9bcdcb30145bee0da6ceb2cdac038939,{},))))))):(jsx(Fragment_293d9760423a245231825532a6975074,{},))))
  )
}


function Fragment_71482ebcca310936b856ecf580dba282 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "events"?.valueOf?.())?(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"4"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "22px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},"S\u1ef1 ki\u1ec7n tham gia"),jsx(RadixThemesBox,{css:({ ["background"] : "white", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "12px", ["width"] : "100%", ["padding"] : "24px" })},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"6"},jsx(Fragment_3313b9eb59c5533bd4461176aeb5b41b,{},),jsx(RadixThemesBox,{css:({ ["display"] : "inline-flex", ["background"] : "#f3f4f6", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["padding"] : "4px", ["gap"] : "4px" })},jsx(Box_1e2870834b5f056d773bbab4f2d14835,{},),jsx(Box_3d012a9cfabaabb08abe34e9d12811db,{},)),jsx(Fragment_ff20d0eda704f84f6f3ecc3c6bc8e216,{},)))))):(jsx(Fragment_880553d749dd4dd1be3fa071760e6064,{},))))
  )
}


function Fragment_206eb5d4be88de67115bb1c1e507b0e1 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "admin_conduct_timeline"?.valueOf?.())?(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"4"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "22px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},"M\u1ed1c th\u1eddi gian phi\u1ebfu \u0111i\u1ec3m r\u00e8n luy\u1ec7n"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["color"] : "#6b7280" })},"C\u1ea5u h\u00ecnh 4 b\u01b0\u1edbc tr\u00ean timeline (minh ch\u1ee9ng \u2192 t\u1ef1 \u0111\u00e1nh gi\u00e1 \u2192 ban c\u00e1n s\u1ef1 \u2192 CVHT). \u00c1p d\u1ee5ng cho h\u1ecdc k\u1ef3 \u0111\u00e3 ch\u1ecdn. \u0110\u1ecbnh d\u1ea1ng: dd/mm/yyyy hh:mm."),jsx(RadixThemesBox,{css:({ ["background"] : "white", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "12px", ["padding"] : "24px", ["width"] : "100%" })},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%", ["maxWidth"] : "640px" }),direction:"column",gap:"4"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* H\u1ecdc k\u1ef3"),jsx(Select__root_2eb61b77968297c73d413c56ca84877e,{},),jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "14px 0", ["borderBottom"] : "1px solid #e5e7eb" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["fontWeight"] : "700", ["color"] : "#1f2937", ["marginBottom"] : "8px" })},"B\u01b0\u1edbc 1"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"T\u00ean b\u01b0\u1edbc"),jsx(Debounceinput_dedb5ad75083a8c755ea33a4bf6577d3,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"B\u1eaft \u0111\u1ea7u (dd/mm/yyyy hh:mm)"),jsx(Debounceinput_c3e2af26f1bf359873bc11831bf2b1d3,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"K\u1ebft th\u00fac (dd/mm/yyyy hh:mm)"),jsx(Debounceinput_daf033754fdc96e29f2b5b43ae984669,{},)),jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "14px 0", ["borderBottom"] : "1px solid #e5e7eb" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["fontWeight"] : "700", ["color"] : "#1f2937", ["marginBottom"] : "8px" })},"B\u01b0\u1edbc 2"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"T\u00ean b\u01b0\u1edbc"),jsx(Debounceinput_6439f12b3467d556bd23463a3439eda4,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"B\u1eaft \u0111\u1ea7u (dd/mm/yyyy hh:mm)"),jsx(Debounceinput_bf50115578fe612e9471ee4a4b7c73bd,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"K\u1ebft th\u00fac (dd/mm/yyyy hh:mm)"),jsx(Debounceinput_2848184a3d2ce468f0c366ff1b130f72,{},)),jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "14px 0", ["borderBottom"] : "1px solid #e5e7eb" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["fontWeight"] : "700", ["color"] : "#1f2937", ["marginBottom"] : "8px" })},"B\u01b0\u1edbc 3"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"T\u00ean b\u01b0\u1edbc"),jsx(Debounceinput_9b3e6ea3c74988dc5146a695f224f1d0,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"B\u1eaft \u0111\u1ea7u (dd/mm/yyyy hh:mm)"),jsx(Debounceinput_529381a8331ab04c3133da63b9591df4,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"K\u1ebft th\u00fac (dd/mm/yyyy hh:mm)"),jsx(Debounceinput_8d47fd8d9a35f2a947dd50ef40aefbc9,{},)),jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "14px 0", ["borderBottom"] : "1px solid #e5e7eb" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["fontWeight"] : "700", ["color"] : "#1f2937", ["marginBottom"] : "8px" })},"B\u01b0\u1edbc 4"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"T\u00ean b\u01b0\u1edbc"),jsx(Debounceinput_0258db4794ec6235d32d1510fd89239b,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"B\u1eaft \u0111\u1ea7u (dd/mm/yyyy hh:mm)"),jsx(Debounceinput_ceceba24488b7b7cc66e5fdff8873095,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"K\u1ebft th\u00fac (dd/mm/yyyy hh:mm)"),jsx(Debounceinput_fcf915094685af3c646bdae145cd5096,{},)),jsx(RadixThemesBox,{css:({ ["width"] : "200px" })},jsx(Button_a6fad7ce98ee048de4481db700297603,{},))))))):(jsx(Fragment_71482ebcca310936b856ecf580dba282,{},))))
  )
}


function Fragment_3acb4d74b6ba55a66fa7a3bbe6e235b6 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "role_management"?.valueOf?.())?(jsx(Fragment_969b3e8f37bbea9ea6150bc28fece0f7,{},)):(jsx(Fragment_206eb5d4be88de67115bb1c1e507b0e1,{},))))
  )
}


function Fragment_a14d95e141a4323fd767d5637b6fd4ad () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "evidence"?.valueOf?.())?(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"4"},jsx(Fragment_265f21a195b0dc4dc19ed007f2fd2f39,{},),jsx(Fragment_4825087903813d4c4fdeb030523e3f8e,{},),jsx(RadixThemesBox,{css:({ ["background"] : "white", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "12px", ["width"] : "100%", ["overflow"] : "hidden", ["position"] : "relative" })},jsx(RadixThemesBox,{css:({ ["padding"] : "16px 18px", ["borderBottom"] : "1px solid #e5e7eb" })},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["flexWrap"] : "wrap" }),direction:"row",justify:"between",gap:"3"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"column",gap:"0"},jsx(Fragment_e481484b0e70c316b06b1f0a2afbbf4c,{},),jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["flexWrap"] : "wrap" }),direction:"row",gap:"2"},jsx(Text_8e2de377a3aac2e9e3e7ac3f4b525aab,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["color"] : "#6b7280" })},"\u2022"),jsx(Text_77e76f365172eccc54e58040eda12034,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["color"] : "#6b7280" })},"\u2022"),jsx(Text_84db5c447968c18c7a5993ff3bc1a4f8,{},))),jsx(Fragment_0b630256d90782375a7752fe4bfe5e58,{},))),jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%", ["minWidth"] : "0" }),direction:"row",gap:"0"},jsx(Box_8696ab88fa1fc9db2a0dbada4e4c99a9,{},),jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%", ["padding"] : "16px", ["position"] : "relative", ["minWidth"] : "0" }),direction:"column",gap:"4"},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["flexWrap"] : "wrap" }),direction:"row",justify:"between",gap:"3"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "18px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},"Danh s\u00e1ch minh ch\u1ee9ng"),jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",direction:"row",gap:"3"},jsx(Fragment_ea1e6bff2d6db7a16f88816696e81df9,{},),jsx(Button_c4b809ba8276fba3517b115a4827a629,{},),jsx(RadixThemesBox,{css:({ ["display"] : "flex", ["alignItems"] : "center", ["gap"] : "4px", ["padding"] : "0 14px", ["height"] : "38px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" })},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#6b7280" })},"T\u1ed5ng s\u1ed1: "),jsx(Text_eb35ab60d861402244d1ec721be75434,{},)),jsx(RadixThemesBox,{css:({ ["position"] : "relative" })},jsx(Button_9d89a725a5df0988bd04431cb0857f95,{},)))),jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["overflowX"] : "auto", ["overflowY"] : "hidden", ["position"] : "relative" })},jsx(RadixThemesBox,{css:({ ["minWidth"] : "1164px", ["width"] : "100%" })},jsx(Box_17d55afa5f7e1a7ea055327efc5179b4,{},),jsx(Fragment_3105c8464f9695214961f79be329256c,{},)))))),jsx(Fragment_f846582f20ef649825a1dafacbb945d6,{},)))):(jsx(Fragment_3acb4d74b6ba55a66fa7a3bbe6e235b6,{},))))
  )
}


function Fragment_cf80bd348ae7f4e6e1c6e60c153b0d22 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "student_detail"?.valueOf?.())?(jsx(Fragment_da2f1848627d3778054dbf89217d2e27,{},)):(jsx(Fragment_a14d95e141a4323fd767d5637b6fd4ad,{},))))
  )
}


function Fragment_8845dc06d13b023c01bdd319be65874c () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},((reflex___state____state__ptit_reflex___state____conduct_state.active_tab_rx_state_?.valueOf?.() === "student_info"?.valueOf?.())?(jsx(Fragment_da2f1848627d3778054dbf89217d2e27,{},)):(jsx(Fragment_cf80bd348ae7f4e6e1c6e60c153b0d22,{},))))
  )
}


function Fragment_3e2a900516bb9f51a0c09803e6005a04 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.loading_rx_state_?(jsx(Fragment,{},jsx(RadixThemesFlex,{css:({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["minHeight"] : "50vh", ["width"] : "100%" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "16px", ["color"] : "#6b7280", ["fontWeight"] : "500" })},"\u0110ang t\u1ea3i d\u1eef li\u1ec7u...")))):(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%", ["minWidth"] : "0" }),direction:"column",gap:"4"},jsx(Fragment_ace4f9daeb0704d294dde9e1d0d362fd,{},),jsx(Fragment_8845dc06d13b023c01bdd319be65874c,{},))))))
  )
}


function Text_084101eb7a6c4fd0ce1a831271349edf () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "18px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},reflex___state____state__ptit_reflex___state____conduct_state.selected_evidence_category_label_rx_state_)
  )
}


function Text_327d1dfb92fd7b563874aafd6678db1c () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_6daf4d54d02429daff2f631861685f13 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.close_evidence_modal", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "22px", ["color"] : "#9ca3af", ["cursor"] : "pointer" }),onClick:on_click_6daf4d54d02429daff2f631861685f13},"\u2715")
  )
}


function Select__root_3d7ddd7ac72691fff15709aab0bddcee () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_3ee9b4bd70307d65c2b512368e5d6976 = useCallback(((_ev_0) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "evidence_award_level", ["value"] : _ev_0 }), ({  })))], [_ev_0], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesSelect.Root,{onValueChange:on_change_3ee9b4bd70307d65c2b512368e5d6976,value:reflex___state____state__ptit_reflex___state____conduct_state.evidence_award_level_rx_state_},jsx(RadixThemesSelect.Trigger,{css:({ ["width"] : "100%" })},),jsx(RadixThemesSelect.Content,{},jsx(RadixThemesSelect.Group,{},"",jsx(RadixThemesSelect.Item,{value:"Gi\u1ea3i Nh\u1ea5t c\u1ea5p H\u1ecdc vi\u1ec7n"},"Gi\u1ea3i Nh\u1ea5t c\u1ea5p H\u1ecdc vi\u1ec7n"),jsx(RadixThemesSelect.Item,{value:"Gi\u1ea3i Nh\u00ec c\u1ea5p H\u1ecdc vi\u1ec7n"},"Gi\u1ea3i Nh\u00ec c\u1ea5p H\u1ecdc vi\u1ec7n"),jsx(RadixThemesSelect.Item,{value:"Gi\u1ea3i Ba c\u1ea5p H\u1ecdc vi\u1ec7n"},"Gi\u1ea3i Ba c\u1ea5p H\u1ecdc vi\u1ec7n"),jsx(RadixThemesSelect.Item,{value:"Gi\u1ea3i khuy\u1ebfn kh\u00edch"},"Gi\u1ea3i khuy\u1ebfn kh\u00edch"))))
  )
}


function Debounceinput_cf63a715ad62a70eb561ff7582be3b3e () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_ba4c3a94e1c6aa2768207b1def0cc1ae = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "evidence_activity_content", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["minHeight"] : "100px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextArea,onChange:on_change_ba4c3a94e1c6aa2768207b1def0cc1ae,placeholder:"Nh\u1eadp N\u1ed9i dung ho\u1ea1t \u0111\u1ed9ng",value:reflex___state____state__ptit_reflex___state____conduct_state.evidence_activity_content_rx_state_},)
  )
}


function Debounceinput_367a062b842557a7f78f128a6d64afe4 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_9e58bc4d769f65ea669b465fe33c5901 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "evidence_participation_time", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_9e58bc4d769f65ea669b465fe33c5901,placeholder:"YYYY-MM-DD",type:"date",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.evidence_participation_time_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.evidence_participation_time_rx_state_ : "")},)
  )
}


function Debounceinput_73660271033d8bc22ffe3bf6457fba25 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_3fa6c62bfd88949a8ff801c495d51ae9 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "evidence_url", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_3fa6c62bfd88949a8ff801c495d51ae9,placeholder:"Nh\u1eadp \u0110\u01b0\u1eddng d\u1eabn",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.evidence_url_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.evidence_url_rx_state_ : "")},)
  )
}


function Comp_441985e882d330c10f2cf7f794fdb280 () {
  const ref_evidence_upload = useRef(null); refs["ref_evidence_upload"] = ref_evidence_upload;
const [addEvents, connectErrors] = useContext(EventLoopContext);
const on_drop_b0cabcb414ba1ea18eb6f7c2c2841277 = useCallback(((_ev_0) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.handle_evidence_upload", ({ ["files"] : _ev_0, ["upload_id"] : "evidence_upload", ["extra_headers"] : ({  }) }), ({  }), "uploadFiles"))], [_ev_0], ({  })))), [addEvents, ReflexEvent])
const on_drop_rejected_2fcedbdc0771e7617b4270e2d1ac8cc9 = useCallback(((_ev_0) => (addEvents([(ReflexEvent("_call_function", ({ ["function"] : (() => (refs['__toast']?.["error"]("", ({ ["title"] : "Files not Accepted", ["description"] : _ev_0.map(((osizayzf) => (osizayzf?.["file"]?.["path"]+": "+osizayzf?.["errors"].map(((wnkiegyk) => wnkiegyk?.["message"])).join(", ")))).join("\n\n"), ["closeButton"] : true, ["style"] : ({ ["whiteSpace"] : "pre-line" }) })))), ["callback"] : null }), ({  })))], [_ev_0], ({  })))), [addEvents, ReflexEvent])
const { getRootProps: xdvxrcsn, getInputProps: udaxihhe, isDragActive: bacghqta} = useDropzone(({ ["onDrop"] : on_drop_b0cabcb414ba1ea18eb6f7c2c2841277, ["multiple"] : false, ["maxFiles"] : 1, ["id"] : "evidence_upload", ["onDropRejected"] : on_drop_rejected_2fcedbdc0771e7617b4270e2d1ac8cc9 }));
const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},jsx(RadixThemesBox,{className:"rx-Upload",css:({ ["width"] : "100%", ["padding"] : "16px", ["border"] : "1px dashed #d92314", ["borderRadius"] : "10px", ["background"] : "#fff5f5", ["cursor"] : "pointer", ["textAlign"] : "center" }),id:"evidence_upload",ref:ref_evidence_upload,...xdvxrcsn()},jsx("input",{type:"file",...udaxihhe()},),jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},"Ch\u1ecdn t\u1ec7p minh ch\u1ee9ng"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["color"] : "#6b7280" })},"B\u1ea5m \u0111\u1ec3 ch\u1ecdn ho\u1eb7c k\u00e9o th\u1ea3 1 t\u1ec7p v\u00e0o \u0111\u00e2y."),jsx(Fragment,{},(!((reflex___state____state__ptit_reflex___state____conduct_state.evidence_file_name_rx_state_?.valueOf?.() === ""?.valueOf?.()))?(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "10px 12px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["fontWeight"] : "600", ["color"] : "#d92314" })},reflex___state____state__ptit_reflex___state____conduct_state.evidence_file_name_rx_state_)))):(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "10px 12px", ["border"] : "1px dashed #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["color"] : "#6b7280" })},"Ch\u01b0a ch\u1ecdn t\u1ec7p n\u00e0o")))))))))
  )
}


function Text_11107b69ade5455d2572429f7effe366 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},reflex___state____state__ptit_reflex___state____conduct_state.evidence_file_name_rx_state_)
  )
}


function Fragment_88a86aa3ca11b1cc9168c06b1f01c95e () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(!((reflex___state____state__ptit_reflex___state____conduct_state.evidence_file_name_rx_state_?.valueOf?.() === ""?.valueOf?.()))?(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["flexWrap"] : "wrap" }),direction:"row",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["color"] : "#6b7280" })},"\u0110\u00e3 ch\u1ecdn:"),jsx(Text_11107b69ade5455d2572429f7effe366,{},)))):(jsx(Fragment,{},))))
  )
}


function Debounceinput_a273821fd2e0e272a5b3b5e5f7ce578f () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_ba4c3a94e1c6aa2768207b1def0cc1ae = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "evidence_activity_content", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_ba4c3a94e1c6aa2768207b1def0cc1ae,placeholder:"Nh\u1eadp N\u1ed9i dung ho\u1ea1t \u0111\u1ed9ng",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.evidence_activity_content_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.evidence_activity_content_rx_state_ : "")},)
  )
}


function Debounceinput_af30c7b333e35759baa26375e5ab3014 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_837bf9fc83305dbd5956ef5bdb9d3a21 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "evidence_event_name", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_837bf9fc83305dbd5956ef5bdb9d3a21,placeholder:"Nh\u1eadp S\u1ef1 ki\u1ec7n",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.evidence_event_name_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.evidence_event_name_rx_state_ : "")},)
  )
}


function Debounceinput_3557360893485d700a8069ac7dbcbf7c () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_92b95ff0febc9f40d3ce12145d0841fa = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "evidence_share_time", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_92b95ff0febc9f40d3ce12145d0841fa,placeholder:"YYYY-MM-DD",type:"date",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.evidence_share_time_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.evidence_share_time_rx_state_ : "")},)
  )
}


function Comp_038f38cf15c06e2a7ca8feb3718d2b85 () {
  const ref_evidence_upload = useRef(null); refs["ref_evidence_upload"] = ref_evidence_upload;
const [addEvents, connectErrors] = useContext(EventLoopContext);
const on_drop_b0cabcb414ba1ea18eb6f7c2c2841277 = useCallback(((_ev_0) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.handle_evidence_upload", ({ ["files"] : _ev_0, ["upload_id"] : "evidence_upload", ["extra_headers"] : ({  }) }), ({  }), "uploadFiles"))], [_ev_0], ({  })))), [addEvents, ReflexEvent])
const on_drop_rejected_51f7597a906ee6a527ceb347e5723946 = useCallback(((_ev_0) => (addEvents([(ReflexEvent("_call_function", ({ ["function"] : (() => (refs['__toast']?.["error"]("", ({ ["title"] : "Files not Accepted", ["description"] : _ev_0.map(((dmioulfl) => (dmioulfl?.["file"]?.["path"]+": "+dmioulfl?.["errors"].map(((lgviwvuc) => lgviwvuc?.["message"])).join(", ")))).join("\n\n"), ["closeButton"] : true, ["style"] : ({ ["whiteSpace"] : "pre-line" }) })))), ["callback"] : null }), ({  })))], [_ev_0], ({  })))), [addEvents, ReflexEvent])
const { getRootProps: zbxordmc, getInputProps: dcmdllti, isDragActive: rjutlsgw} = useDropzone(({ ["onDrop"] : on_drop_b0cabcb414ba1ea18eb6f7c2c2841277, ["multiple"] : false, ["maxFiles"] : 1, ["id"] : "evidence_upload", ["onDropRejected"] : on_drop_rejected_51f7597a906ee6a527ceb347e5723946 }));
const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},jsx(RadixThemesBox,{className:"rx-Upload",css:({ ["width"] : "100%", ["padding"] : "16px", ["border"] : "1px dashed #d92314", ["borderRadius"] : "10px", ["background"] : "#fff5f5", ["cursor"] : "pointer", ["textAlign"] : "center" }),id:"evidence_upload",ref:ref_evidence_upload,...zbxordmc()},jsx("input",{type:"file",...dcmdllti()},),jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},"Ch\u1ecdn t\u1ec7p minh ch\u1ee9ng"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["color"] : "#6b7280" })},"B\u1ea5m \u0111\u1ec3 ch\u1ecdn ho\u1eb7c k\u00e9o th\u1ea3 1 t\u1ec7p v\u00e0o \u0111\u00e2y."),jsx(Fragment,{},(!((reflex___state____state__ptit_reflex___state____conduct_state.evidence_file_name_rx_state_?.valueOf?.() === ""?.valueOf?.()))?(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "10px 12px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["fontWeight"] : "600", ["color"] : "#d92314" })},reflex___state____state__ptit_reflex___state____conduct_state.evidence_file_name_rx_state_)))):(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "10px 12px", ["border"] : "1px dashed #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["color"] : "#6b7280" })},"Ch\u01b0a ch\u1ecdn t\u1ec7p n\u00e0o")))))))))
  )
}


function Select__root_ea3d7be3534750c7e4afbeb248d278af () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_2cdf20e79dbd8661dc1df2b3f564aafc = useCallback(((_ev_0) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "evidence_social_type", ["value"] : _ev_0 }), ({  })))], [_ev_0], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesSelect.Root,{onValueChange:on_change_2cdf20e79dbd8661dc1df2b3f564aafc,value:reflex___state____state__ptit_reflex___state____conduct_state.evidence_social_type_rx_state_},jsx(RadixThemesSelect.Trigger,{css:({ ["width"] : "100%" })},),jsx(RadixThemesSelect.Content,{},jsx(RadixThemesSelect.Group,{},"",jsx(RadixThemesSelect.Item,{value:"Hi\u1ebfn m\u00e1u nh\u00e2n \u0111\u1ea1o"},"Hi\u1ebfn m\u00e1u nh\u00e2n \u0111\u1ea1o"),jsx(RadixThemesSelect.Item,{value:"\u1ee6ng h\u1ed9 thi\u00ean tai l\u0169 l\u1ee5t"},"\u1ee6ng h\u1ed9 thi\u00ean tai l\u0169 l\u1ee5t"),jsx(RadixThemesSelect.Item,{value:"T\u00ecnh nguy\u1ec7n h\u1ed7 tr\u1ee3 c\u1ed9ng \u0111\u1ed3ng"},"T\u00ecnh nguy\u1ec7n h\u1ed7 tr\u1ee3 c\u1ed9ng \u0111\u1ed3ng"))))
  )
}


function Comp_7fe840cbe94b98ca56aa0425c5055592 () {
  const ref_evidence_upload = useRef(null); refs["ref_evidence_upload"] = ref_evidence_upload;
const [addEvents, connectErrors] = useContext(EventLoopContext);
const on_drop_b0cabcb414ba1ea18eb6f7c2c2841277 = useCallback(((_ev_0) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.handle_evidence_upload", ({ ["files"] : _ev_0, ["upload_id"] : "evidence_upload", ["extra_headers"] : ({  }) }), ({  }), "uploadFiles"))], [_ev_0], ({  })))), [addEvents, ReflexEvent])
const on_drop_rejected_bedc1fe7e7d4fcbcbc646af9fb7688c4 = useCallback(((_ev_0) => (addEvents([(ReflexEvent("_call_function", ({ ["function"] : (() => (refs['__toast']?.["error"]("", ({ ["title"] : "Files not Accepted", ["description"] : _ev_0.map(((pmuoeieh) => (pmuoeieh?.["file"]?.["path"]+": "+pmuoeieh?.["errors"].map(((xrrixsns) => xrrixsns?.["message"])).join(", ")))).join("\n\n"), ["closeButton"] : true, ["style"] : ({ ["whiteSpace"] : "pre-line" }) })))), ["callback"] : null }), ({  })))], [_ev_0], ({  })))), [addEvents, ReflexEvent])
const { getRootProps: miuwrhvk, getInputProps: tufrxhfo, isDragActive: yybhbzkm} = useDropzone(({ ["onDrop"] : on_drop_b0cabcb414ba1ea18eb6f7c2c2841277, ["multiple"] : false, ["maxFiles"] : 1, ["id"] : "evidence_upload", ["onDropRejected"] : on_drop_rejected_bedc1fe7e7d4fcbcbc646af9fb7688c4 }));
const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},jsx(RadixThemesBox,{className:"rx-Upload",css:({ ["width"] : "100%", ["padding"] : "16px", ["border"] : "1px dashed #d92314", ["borderRadius"] : "10px", ["background"] : "#fff5f5", ["cursor"] : "pointer", ["textAlign"] : "center" }),id:"evidence_upload",ref:ref_evidence_upload,...miuwrhvk()},jsx("input",{type:"file",...tufrxhfo()},),jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},"Ch\u1ecdn t\u1ec7p minh ch\u1ee9ng"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["color"] : "#6b7280" })},"B\u1ea5m \u0111\u1ec3 ch\u1ecdn ho\u1eb7c k\u00e9o th\u1ea3 1 t\u1ec7p v\u00e0o \u0111\u00e2y."),jsx(Fragment,{},(!((reflex___state____state__ptit_reflex___state____conduct_state.evidence_file_name_rx_state_?.valueOf?.() === ""?.valueOf?.()))?(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "10px 12px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["fontWeight"] : "600", ["color"] : "#d92314" })},reflex___state____state__ptit_reflex___state____conduct_state.evidence_file_name_rx_state_)))):(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "10px 12px", ["border"] : "1px dashed #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["color"] : "#6b7280" })},"Ch\u01b0a ch\u1ecdn t\u1ec7p n\u00e0o")))))))))
  )
}


function Select__root_963977ce6742d60a6dbf0138a8875168 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_169fd851c39d75de2fea04d12480d324 = useCallback(((_ev_0) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "evidence_residence_type", ["value"] : _ev_0 }), ({  })))], [_ev_0], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesSelect.Root,{onValueChange:on_change_169fd851c39d75de2fea04d12480d324,value:reflex___state____state__ptit_reflex___state____conduct_state.evidence_residence_type_rx_state_},jsx(RadixThemesSelect.Trigger,{css:({ ["width"] : "100%" })},),jsx(RadixThemesSelect.Content,{},jsx(RadixThemesSelect.Group,{},"",jsx(RadixThemesSelect.Item,{value:"N\u1ed9i tr\u00fa"},"N\u1ed9i tr\u00fa"),jsx(RadixThemesSelect.Item,{value:"Ngo\u1ea1i tr\u00fa"},"Ngo\u1ea1i tr\u00fa"))))
  )
}


function Debounceinput_6dcb175a08214f9873fd07e2eb6e021e () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_7e56eca5cd5ad94c5585fe7447528785 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "evidence_dormitory", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_7e56eca5cd5ad94c5585fe7447528785,placeholder:"Nh\u1eadp K\u00fd t\u00fac x\u00e1",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.evidence_dormitory_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.evidence_dormitory_rx_state_ : "")},)
  )
}


function Debounceinput_eaeb048b5751ff820924352f6beda29f () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_f48a9514aef332d28a16da8de862dfd1 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "evidence_room_number", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_f48a9514aef332d28a16da8de862dfd1,placeholder:"Nh\u1eadp S\u1ed1 ph\u00f2ng",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.evidence_room_number_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.evidence_room_number_rx_state_ : "")},)
  )
}


function Debounceinput_7f23c71bde29eb5b80ca2590a30b24af () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_41709d44eba80cbe023bed885da4caba = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "evidence_city", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_41709d44eba80cbe023bed885da4caba,placeholder:"Nh\u1eadp T\u1ec9nh/Th\u00e0nh ph\u1ed1",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.evidence_city_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.evidence_city_rx_state_ : "")},)
  )
}


function Debounceinput_38237cf28e8f65bb8567b17a25ed31d7 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_6d99c0a594880421322a48f73b69c048 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "evidence_district", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_6d99c0a594880421322a48f73b69c048,placeholder:"Nh\u1eadp Qu\u1eadn/Huy\u1ec7n",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.evidence_district_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.evidence_district_rx_state_ : "")},)
  )
}


function Debounceinput_f608967e3b37e8a3475213484ed5869e () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_5d672fb45c668a1aef563638116f911d = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "evidence_ward", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_5d672fb45c668a1aef563638116f911d,placeholder:"Nh\u1eadp X\u00e3/Ph\u01b0\u1eddng",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.evidence_ward_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.evidence_ward_rx_state_ : "")},)
  )
}


function Debounceinput_ecf25833aef2db2426266545ffd26836 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_570e493ad06cc33e8940f158bb9ea8dc = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "evidence_street_address", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_570e493ad06cc33e8940f158bb9ea8dc,placeholder:"Nh\u1eadp S\u1ed1 nh\u00e0, \u0111\u01b0\u1eddng ph\u1ed1",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.evidence_street_address_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.evidence_street_address_rx_state_ : "")},)
  )
}


function Debounceinput_0246f7b44ad5cfe79f23bb8bbf7ee280 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_bac00cdd6cd695d0fcc7c0c0961e0db1 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "evidence_host_name", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_bac00cdd6cd695d0fcc7c0c0961e0db1,placeholder:"Nh\u1eadp H\u1ecd t\u00ean ch\u1ee7 nh\u00e0/tr\u1ecd/ng\u01b0\u1eddi th\u00e2n",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.evidence_host_name_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.evidence_host_name_rx_state_ : "")},)
  )
}


function Debounceinput_b3b5a377c3cc2f5419f28da6ec9108bf () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_dcc6d46e12e9d2f3aa7abfb9a5a7bff2 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_form_value", ({ ["field_name"] : "evidence_host_phone", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_dcc6d46e12e9d2f3aa7abfb9a5a7bff2,placeholder:"Nh\u1eadp S\u0110T c\u1ee7a ch\u1ee7 nh\u00e0/tr\u1ecd/ng\u01b0\u1eddi th\u00e2n",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.evidence_host_phone_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.evidence_host_phone_rx_state_ : "")},)
  )
}


function Fragment_bd095790a0ca1473a3d175b538dc1e7e () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},((reflex___state____state__ptit_reflex___state____conduct_state.evidence_residence_type_rx_state_?.valueOf?.() === "N\u1ed9i tr\u00fa"?.valueOf?.())?(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%", ["flexWrap"] : "wrap" }),direction:"row",gap:"4"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["flex"] : "1" }),direction:"column",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* K\u00fd t\u00fac x\u00e1"),jsx(Debounceinput_6dcb175a08214f9873fd07e2eb6e021e,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["flex"] : "1" }),direction:"column",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* S\u1ed1 ph\u00f2ng"),jsx(Debounceinput_eaeb048b5751ff820924352f6beda29f,{},))))):(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"4"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%", ["flexWrap"] : "wrap" }),direction:"row",gap:"4"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["flex"] : "1" }),direction:"column",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* T\u1ec9nh/Th\u00e0nh ph\u1ed1"),jsx(Debounceinput_7f23c71bde29eb5b80ca2590a30b24af,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["flex"] : "1" }),direction:"column",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* Qu\u1eadn/Huy\u1ec7n"),jsx(Debounceinput_38237cf28e8f65bb8567b17a25ed31d7,{},))),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%", ["flexWrap"] : "wrap" }),direction:"row",gap:"4"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["flex"] : "1" }),direction:"column",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* X\u00e3/Ph\u01b0\u1eddng"),jsx(Debounceinput_f608967e3b37e8a3475213484ed5869e,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["flex"] : "1" }),direction:"column",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* S\u1ed1 nh\u00e0, \u0111\u01b0\u1eddng ph\u1ed1"),jsx(Debounceinput_ecf25833aef2db2426266545ffd26836,{},))),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%", ["flexWrap"] : "wrap" }),direction:"row",gap:"4"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["flex"] : "1" }),direction:"column",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* H\u1ecd t\u00ean ch\u1ee7 nh\u00e0/tr\u1ecd/ng\u01b0\u1eddi th\u00e2n"),jsx(Debounceinput_0246f7b44ad5cfe79f23bb8bbf7ee280,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["flex"] : "1" }),direction:"column",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* S\u0110T c\u1ee7a ch\u1ee7 nh\u00e0/tr\u1ecd/ng\u01b0\u1eddi th\u00e2n"),jsx(Debounceinput_b3b5a377c3cc2f5419f28da6ec9108bf,{},))))))))
  )
}


function Comp_4bb368fac829129e05da59d155d4d538 () {
  const ref_evidence_upload = useRef(null); refs["ref_evidence_upload"] = ref_evidence_upload;
const [addEvents, connectErrors] = useContext(EventLoopContext);
const on_drop_b0cabcb414ba1ea18eb6f7c2c2841277 = useCallback(((_ev_0) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.handle_evidence_upload", ({ ["files"] : _ev_0, ["upload_id"] : "evidence_upload", ["extra_headers"] : ({  }) }), ({  }), "uploadFiles"))], [_ev_0], ({  })))), [addEvents, ReflexEvent])
const on_drop_rejected_93682d868b73b9096d5e1b100bdceaa6 = useCallback(((_ev_0) => (addEvents([(ReflexEvent("_call_function", ({ ["function"] : (() => (refs['__toast']?.["error"]("", ({ ["title"] : "Files not Accepted", ["description"] : _ev_0.map(((iyukdjnf) => (iyukdjnf?.["file"]?.["path"]+": "+iyukdjnf?.["errors"].map(((oaxxiqyf) => oaxxiqyf?.["message"])).join(", ")))).join("\n\n"), ["closeButton"] : true, ["style"] : ({ ["whiteSpace"] : "pre-line" }) })))), ["callback"] : null }), ({  })))], [_ev_0], ({  })))), [addEvents, ReflexEvent])
const { getRootProps: bdeufzvn, getInputProps: mlheqpcy, isDragActive: tcmmtoqi} = useDropzone(({ ["onDrop"] : on_drop_b0cabcb414ba1ea18eb6f7c2c2841277, ["multiple"] : false, ["maxFiles"] : 1, ["id"] : "evidence_upload", ["onDropRejected"] : on_drop_rejected_93682d868b73b9096d5e1b100bdceaa6 }));
const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},jsx(RadixThemesBox,{className:"rx-Upload",css:({ ["width"] : "100%", ["padding"] : "16px", ["border"] : "1px dashed #d92314", ["borderRadius"] : "10px", ["background"] : "#fff5f5", ["cursor"] : "pointer", ["textAlign"] : "center" }),id:"evidence_upload",ref:ref_evidence_upload,...bdeufzvn()},jsx("input",{type:"file",...mlheqpcy()},),jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},"Ch\u1ecdn t\u1ec7p minh ch\u1ee9ng"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["color"] : "#6b7280" })},"B\u1ea5m \u0111\u1ec3 ch\u1ecdn ho\u1eb7c k\u00e9o th\u1ea3 1 t\u1ec7p v\u00e0o \u0111\u00e2y."),jsx(Fragment,{},(!((reflex___state____state__ptit_reflex___state____conduct_state.evidence_file_name_rx_state_?.valueOf?.() === ""?.valueOf?.()))?(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "10px 12px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["fontWeight"] : "600", ["color"] : "#d92314" })},reflex___state____state__ptit_reflex___state____conduct_state.evidence_file_name_rx_state_)))):(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "10px 12px", ["border"] : "1px dashed #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["color"] : "#6b7280" })},"Ch\u01b0a ch\u1ecdn t\u1ec7p n\u00e0o")))))))))
  )
}


function Fragment_f3540511d464df12795dd55fa53924d4 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},((reflex___state____state__ptit_reflex___state____conduct_state.selected_evidence_category_rx_state_?.valueOf?.() === "social_work"?.valueOf?.())?(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"3"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* Tham gia c\u00f4ng t\u00e1c x\u00e3 h\u1ed9i"),jsx(Select__root_ea3d7be3534750c7e4afbeb248d278af,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* Ng\u00e0y tham gia"),jsx(Debounceinput_367a062b842557a7f78f128a6d64afe4,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"\u0110\u01b0\u1eddng d\u1eabn"),jsx(Debounceinput_73660271033d8bc22ffe3bf6457fba25,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* T\u1eadp tin minh ch\u1ee9ng"),jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"2"},jsx(Comp_7fe840cbe94b98ca56aa0425c5055592,{},),jsx(Fragment_88a86aa3ca11b1cc9168c06b1f01c95e,{},))))):(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"3"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* Ph\u00e2n lo\u1ea1i c\u01b0 tr\u00fa"),jsx(Select__root_963977ce6742d60a6dbf0138a8875168,{},),jsx(Fragment_bd095790a0ca1473a3d175b538dc1e7e,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* T\u1eadp tin minh ch\u1ee9ng"),jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"2"},jsx(Comp_4bb368fac829129e05da59d155d4d538,{},),jsx(Fragment_88a86aa3ca11b1cc9168c06b1f01c95e,{},)))))))
  )
}


function Fragment_a1cfc9fcba830760dfa559a9b8d998db () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},((reflex___state____state__ptit_reflex___state____conduct_state.selected_evidence_category_rx_state_?.valueOf?.() === "positive_promotion"?.valueOf?.())?(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"3"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* N\u1ed9i dung ho\u1ea1t \u0111\u1ed9ng"),jsx(Debounceinput_a273821fd2e0e272a5b3b5e5f7ce578f,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"S\u1ef1 ki\u1ec7n"),jsx(Debounceinput_af30c7b333e35759baa26375e5ab3014,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* Ng\u00e0y chia s\u1ebb"),jsx(Debounceinput_3557360893485d700a8069ac7dbcbf7c,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"\u0110\u01b0\u1eddng d\u1eabn"),jsx(Debounceinput_73660271033d8bc22ffe3bf6457fba25,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* T\u1eadp tin minh ch\u1ee9ng"),jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"2"},jsx(Comp_038f38cf15c06e2a7ca8feb3718d2b85,{},),jsx(Fragment_88a86aa3ca11b1cc9168c06b1f01c95e,{},))))):(jsx(Fragment_f3540511d464df12795dd55fa53924d4,{},))))
  )
}


function Fragment_667eb9f2cc5102dfbab387a70f4d59b6 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},((reflex___state____state__ptit_reflex___state____conduct_state.selected_evidence_category_rx_state_?.valueOf?.() === "special_achievement"?.valueOf?.())?(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"3"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* C\u1ea5p \u0111\u1ea1t gi\u1ea3i"),jsx(Select__root_3d7ddd7ac72691fff15709aab0bddcee,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* N\u1ed9i dung ho\u1ea1t \u0111\u1ed9ng"),jsx(Debounceinput_cf63a715ad62a70eb561ff7582be3b3e,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* Ng\u00e0y tham gia"),jsx(Debounceinput_367a062b842557a7f78f128a6d64afe4,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"\u0110\u01b0\u1eddng d\u1eabn"),jsx(Debounceinput_73660271033d8bc22ffe3bf6457fba25,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* T\u1eadp tin minh ch\u1ee9ng"),jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"2"},jsx(Comp_441985e882d330c10f2cf7f794fdb280,{},),jsx(Fragment_88a86aa3ca11b1cc9168c06b1f01c95e,{},))))):(jsx(Fragment_a1cfc9fcba830760dfa559a9b8d998db,{},))))
  )
}


function Button_e01a382cf6a3d5f6f94a266955a218c6 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_6daf4d54d02429daff2f631861685f13 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.close_evidence_modal", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : "white", ["color"] : "#1f2937", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:on_click_6daf4d54d02429daff2f631861685f13},"H\u1ee7y")
  )
}


function Button_9c45f74a09f2f8a5703f8c96e5df77e6 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_fa2fc45cd7ce9def2348829edb1a2c64 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.submit_evidence", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : "#d92314", ["color"] : "white", ["border"] : "none", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:on_click_fa2fc45cd7ce9def2348829edb1a2c64},"Th\u00eam m\u1edbi")
  )
}


function Fragment_b304926424c1a2cba1179c91f6144ff4 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.evidence_modal_open_rx_state_?(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["position"] : "fixed", ["inset"] : "0", ["background"] : "rgba(15, 23, 42, 0.45)", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["padding"] : "24px", ["zIndex"] : "100" })},jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["maxWidth"] : "960px", ["maxHeight"] : "calc(100vh - 48px)", ["background"] : "white", ["borderRadius"] : "14px", ["boxShadow"] : "0 24px 60px rgba(15, 23, 42, 0.18)", ["display"] : "flex", ["flexDirection"] : "column" })},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["padding"] : "20px 24px", ["borderBottom"] : "1px solid #e5e7eb" }),direction:"row",justify:"between",gap:"3"},jsx(Text_084101eb7a6c4fd0ce1a831271349edf,{},),jsx(Text_327d1dfb92fd7b563874aafd6678db1c,{},)),jsx(RadixThemesBox,{css:({ ["padding"] : "24px", ["flex"] : "1", ["minHeight"] : "0", ["overflowY"] : "auto" })},jsx(Fragment_667eb9f2cc5102dfbab387a70f4d59b6,{},)),jsx(RadixThemesBox,{css:({ ["padding"] : "0 24px 24px" })},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"row",justify:"center",gap:"4"},jsx(Button_e01a382cf6a3d5f6f94a266955a218c6,{},),jsx(Button_9c45f74a09f2f8a5703f8c96e5df77e6,{},))))))):(jsx(Fragment,{},))))
  )
}


function Text_73f4c7eedc6ce949a9b50f901dda8553 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "18px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},reflex___state____state__ptit_reflex___state____conduct_state.selected_evidence_title_rx_state_)
  )
}


function Text_930e78c92524144b1ff7e8e4f4f034cb () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_580a6aa05061a3883f732d86cb160cf1 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.close_evidence_detail", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "22px", ["color"] : "#9ca3af", ["cursor"] : "pointer" }),onClick:on_click_580a6aa05061a3883f732d86cb160cf1},"\u2715")
  )
}


function Text_1fddf225f02e10efb3f7cbd9448c3f95 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#d92314", ["fontSize"] : "13px", ["fontWeight"] : "700" })},reflex___state____state__ptit_reflex___state____conduct_state.selected_evidence_status_label_rx_state_)
  )
}


function Flex_0c77b829194b63ef6e18712137293389 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"4"},jsx(Text_1fddf225f02e10efb3f7cbd9448c3f95,{},),Array.prototype.map.call(reflex___state____state__ptit_reflex___state____conduct_state.selected_evidence_fields_rx_state_ ?? [],((item_rx_state_,index_6a6b2ff138465bcfaefdfcd0efbd14e4)=>(jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",key:index_6a6b2ff138465bcfaefdfcd0efbd14e4,gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["fontWeight"] : "700", ["color"] : "#6b7280" })},item_rx_state_?.["label"]),jsx(Fragment,{},(isTrue(item_rx_state_?.["is_link"])?(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "12px 14px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "#f8fafc" })},jsx(RadixThemesLink,{asChild:true,css:({ ["color"] : "#d92314", ["fontWeight"] : "600", ["fontSize"] : "15px", ["textDecoration"] : "underline", ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })},jsx(ReactRouterLink,{target:(true ? "_blank" : ""),to:item_rx_state_?.["value"]},item_rx_state_?.["value"]))))):(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "12px 14px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "#f8fafc" })},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["color"] : "#1f2937" })},item_rx_state_?.["value"])))))))))))
  )
}


function Button_9e43d78d52a96a9626ce46dbba7db42d () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_a787a65e1f51dec7d1ce42e0577ddb55 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.approve_selected_evidence_class", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : "#d92314", ["color"] : "white", ["border"] : "none", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:on_click_a787a65e1f51dec7d1ce42e0577ddb55},"Duy\u1ec7t")
  )
}


function Fragment_f368959d96ec7884b1a00416741685ed () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.selected_evidence_can_class_review_rx_state_?(jsx(Fragment,{},jsx(Button_9e43d78d52a96a9626ce46dbba7db42d,{},))):(jsx(Fragment,{},))))
  )
}


function Button_209490996fead1acc1284a85cc900d9b () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_7b046b4b872353c01cebfa1fa179d687 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.approve_selected_evidence_advisor", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : "#15803d", ["color"] : "white", ["border"] : "none", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:on_click_7b046b4b872353c01cebfa1fa179d687},"Duy\u1ec7t")
  )
}


function Fragment_a3f9c90a4a67c6c1a6a8c9b492856f1d () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.selected_evidence_can_advisor_review_rx_state_?(jsx(Fragment,{},jsx(Button_209490996fead1acc1284a85cc900d9b,{},))):(jsx(Fragment,{},))))
  )
}


function Button_45095fda9310f2f29fa15a9f302119be () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_4bae2b441c3e78d952feb67299ecde5e = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.reject_selected_evidence", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : "#fff1f2", ["color"] : "#d92314", ["border"] : "1px solid #fecdd3", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:on_click_4bae2b441c3e78d952feb67299ecde5e},"T\u1eeb ch\u1ed1i")
  )
}


function Fragment_2559883630ec6221e475dc062bbec798 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.selected_evidence_can_advisor_review_rx_state_?(jsx(Fragment,{},jsx(Button_45095fda9310f2f29fa15a9f302119be,{},))):(jsx(Fragment,{},))))
  )
}


function Fragment_6f6dee605dc04e9dc9fb088a94480d9f () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.selected_evidence_can_class_review_rx_state_?(jsx(Fragment,{},jsx(Button_45095fda9310f2f29fa15a9f302119be,{},))):(jsx(Fragment_2559883630ec6221e475dc062bbec798,{},))))
  )
}


function Button_f183d7023375d15e05d2efc47b34a764 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_580a6aa05061a3883f732d86cb160cf1 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.close_evidence_detail", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : "white", ["color"] : "#1f2937", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:on_click_580a6aa05061a3883f732d86cb160cf1},"\u0110\u00f3ng")
  )
}


function Fragment_9238e3c2def3f8d963fefbc7b5897fe1 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.evidence_detail_open_rx_state_?(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["position"] : "fixed", ["inset"] : "0", ["background"] : "rgba(15, 23, 42, 0.45)", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["padding"] : "24px", ["zIndex"] : "100" })},jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["maxWidth"] : "820px", ["maxHeight"] : "calc(100vh - 48px)", ["background"] : "white", ["borderRadius"] : "14px", ["boxShadow"] : "0 24px 60px rgba(15, 23, 42, 0.18)", ["display"] : "flex", ["flexDirection"] : "column" })},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["padding"] : "20px 24px", ["borderBottom"] : "1px solid #e5e7eb" }),direction:"row",justify:"between",gap:"3"},jsx(Text_73f4c7eedc6ce949a9b50f901dda8553,{},),jsx(Text_930e78c92524144b1ff7e8e4f4f034cb,{},)),jsx(RadixThemesBox,{css:({ ["padding"] : "24px", ["flex"] : "1", ["minHeight"] : "0", ["overflowY"] : "auto" })},jsx(Flex_0c77b829194b63ef6e18712137293389,{},)),jsx(RadixThemesBox,{css:({ ["padding"] : "0 24px 24px" })},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"row",justify:"end",gap:"3"},jsx(Fragment_f368959d96ec7884b1a00416741685ed,{},),jsx(Fragment_a3f9c90a4a67c6c1a6a8c9b492856f1d,{},),jsx(Fragment_6f6dee605dc04e9dc9fb088a94480d9f,{},),jsx(Button_f183d7023375d15e05d2efc47b34a764,{},))))))):(jsx(Fragment,{},))))
  )
}


function Text_21b9abe53f07613277f4a454444077fa () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_cc3da0d6a7bd7da627474ba6621cbbd6 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.close_event_detail", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "22px", ["color"] : "#9ca3af", ["cursor"] : "pointer" }),onClick:on_click_cc3da0d6a7bd7da627474ba6621cbbd6},"\u2715")
  )
}


function Text_7c4647b5c449da5e4725a85eb1f63ec8 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["fontWeight"] : "700", ["color"] : "#6d28d9" })},reflex___state____state__ptit_reflex___state____conduct_state.selected_event_type_label_rx_state_)
  )
}


function Text_155016c02dbc3549dd9efb136009b700 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#1f2937" })},reflex___state____state__ptit_reflex___state____conduct_state.selected_event_name_rx_state_)
  )
}


function Text_89d71029ae951f6930da836dc31ff693 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#1f2937" })},reflex___state____state__ptit_reflex___state____conduct_state.selected_event_start_time_rx_state_)
  )
}


function Text_85c20af23a4d78418fcf3a3581c98a3b () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#1f2937" })},reflex___state____state__ptit_reflex___state____conduct_state.selected_event_end_time_rx_state_)
  )
}


function Text_3c3322cc09261e48fa79860a1b2d7c50 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#1f2937" })},reflex___state____state__ptit_reflex___state____conduct_state.selected_event_location_rx_state_)
  )
}


function Text_07008a7d3f8ad161e669829b797f7814 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#1f2937" })},reflex___state____state__ptit_reflex___state____conduct_state.selected_event_counts_to_score_rx_state_)
  )
}


function Text_dad707655256c547a2b2620080375ae3 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#1f2937" })},reflex___state____state__ptit_reflex___state____conduct_state.selected_event_note_rx_state_)
  )
}


function Button_b737a885cf5ec50984cf39f7fbc1d124 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_cc3da0d6a7bd7da627474ba6621cbbd6 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.close_event_detail", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : "white", ["color"] : "#1f2937", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:on_click_cc3da0d6a7bd7da627474ba6621cbbd6},"\u0110\u00f3ng")
  )
}


function Fragment_12ffb2a25887c9a4c43515206bb9d992 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.event_modal_open_rx_state_?(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["position"] : "fixed", ["inset"] : "0", ["background"] : "rgba(15, 23, 42, 0.45)", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["padding"] : "24px", ["zIndex"] : "100" })},jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["maxWidth"] : "760px", ["maxHeight"] : "calc(100vh - 48px)", ["background"] : "white", ["borderRadius"] : "14px", ["boxShadow"] : "0 24px 60px rgba(15, 23, 42, 0.18)", ["display"] : "flex", ["flexDirection"] : "column" })},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["padding"] : "20px 24px", ["borderBottom"] : "1px solid #e5e7eb" }),direction:"row",justify:"between",gap:"3"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "18px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},"Chi ti\u1ebft l\u1ecbch"),jsx(Text_21b9abe53f07613277f4a454444077fa,{},)),jsx(RadixThemesBox,{css:({ ["padding"] : "24px", ["flex"] : "1", ["minHeight"] : "0", ["overflowY"] : "auto" })},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"4"},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",direction:"row",gap:"3"},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#6b7280", ["fontWeight"] : "700" })},"Lo\u1ea1i s\u1ef1 ki\u1ec7n:"),jsx(RadixThemesBox,{css:({ ["padding"] : "6px 12px", ["borderRadius"] : "999px", ["background"] : "#e9d5ff" })},jsx(Text_7c4647b5c449da5e4725a85eb1f63ec8,{},))),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"row",gap:"3"},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#6b7280", ["fontWeight"] : "700" })},"T\u00ean s\u1ef1 ki\u1ec7n:"),jsx(Text_155016c02dbc3549dd9efb136009b700,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"row",gap:"3"},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#6b7280", ["fontWeight"] : "700" })},"Th\u1eddi gian b\u1eaft \u0111\u1ea7u:"),jsx(Text_89d71029ae951f6930da836dc31ff693,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"row",gap:"3"},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#6b7280", ["fontWeight"] : "700" })},"Th\u1eddi gian k\u1ebft th\u00fac:"),jsx(Text_85c20af23a4d78418fcf3a3581c98a3b,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"row",gap:"3"},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#6b7280", ["fontWeight"] : "700" })},"\u0110\u1ecba \u0111i\u1ec3m:"),jsx(Text_3c3322cc09261e48fa79860a1b2d7c50,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"row",gap:"3"},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#6b7280", ["fontWeight"] : "700" })},"Tham gia s\u1ef1 ki\u1ec7n \u0111\u01b0\u1ee3c t\u00ednh \u0111i\u1ec3m r\u00e8n luy\u1ec7n?:"),jsx(Text_07008a7d3f8ad161e669829b797f7814,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"row",gap:"3"},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#6b7280", ["fontWeight"] : "700" })},"Ghi ch\u00fa:"),jsx(Text_dad707655256c547a2b2620080375ae3,{},)))),jsx(RadixThemesBox,{css:({ ["padding"] : "0 24px 24px" })},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"row",justify:"center",gap:"3"},jsx(Button_b737a885cf5ec50984cf39f7fbc1d124,{},))))))):(jsx(Fragment,{},))))
  )
}


function Text_7c8643a0c03f7f2d271c0eb8a31364d4 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "28px", ["fontWeight"] : "800", ["color"] : "#1f2937" })},((reflex___state____state__ptit_reflex___state____conduct_state.auth_mode_rx_state_?.valueOf?.() === "login"?.valueOf?.()) ? "\u0110\u0103ng nh\u1eadp h\u1ec7 th\u1ed1ng" : "\u0110\u0103ng k\u00fd t\u00e0i kho\u1ea3n"))
  )
}


function Text_d22536746bf96b64b5f3cd05af99230a () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["color"] : "#6b7280", ["textAlign"] : "center" })},((reflex___state____state__ptit_reflex___state____conduct_state.auth_mode_rx_state_?.valueOf?.() === "login"?.valueOf?.()) ? "Nh\u1eadp t\u00e0i kho\u1ea3n c\u1ee7a b\u1ea1n; h\u1ec7 th\u1ed1ng nh\u1eadn di\u1ec7n vai tr\u00f2 theo d\u1eef li\u1ec7u t\u00e0i kho\u1ea3n." : "T\u00e0i kho\u1ea3n m\u1edbi m\u1eb7c \u0111\u1ecbnh c\u00f3 quy\u1ec1n Sinh vi\u00ean. Admin c\u00f3 th\u1ec3 c\u1ea5p m\u1ecdi quy\u1ec1n; c\u1ed1 v\u1ea5n ch\u1ec9 c\u1ea5p Ban c\u00e1n s\u1ef1 cho sinh vi\u00ean."))
  )
}


function Button_6652e350c055b10465602d6ca2cedcd5 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_c10ac661ea2c549a85a196a69d2fa09f = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.show_login_form", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : ((reflex___state____state__ptit_reflex___state____conduct_state.auth_mode_rx_state_?.valueOf?.() === "login"?.valueOf?.()) ? "#d92314" : "white"), ["color"] : ((reflex___state____state__ptit_reflex___state____conduct_state.auth_mode_rx_state_?.valueOf?.() === "login"?.valueOf?.()) ? "white" : "#1f2937"), ["border"] : ((reflex___state____state__ptit_reflex___state____conduct_state.auth_mode_rx_state_?.valueOf?.() === "login"?.valueOf?.()) ? "none" : "1px solid #e5e7eb"), ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:on_click_c10ac661ea2c549a85a196a69d2fa09f},"\u0110\u0103ng nh\u1eadp")
  )
}


function Button_f2e9d294f6ffe21813037a6ceeac1a50 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_a462372720e32655ca315601e7ddf510 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.show_register_form", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : ((reflex___state____state__ptit_reflex___state____conduct_state.auth_mode_rx_state_?.valueOf?.() === "register"?.valueOf?.()) ? "#d92314" : "white"), ["color"] : ((reflex___state____state__ptit_reflex___state____conduct_state.auth_mode_rx_state_?.valueOf?.() === "register"?.valueOf?.()) ? "white" : "#1f2937"), ["border"] : ((reflex___state____state__ptit_reflex___state____conduct_state.auth_mode_rx_state_?.valueOf?.() === "register"?.valueOf?.()) ? "none" : "1px solid #e5e7eb"), ["borderRadius"] : "8px", ["height"] : "38px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:on_click_a462372720e32655ca315601e7ddf510},"\u0110\u0103ng k\u00fd")
  )
}


function Debounceinput_a303e9cf05db1f7c640ccd8f11986ccb () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_777547cc3966de95690db7fdd378f37a = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_login_username", ({ ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_777547cc3966de95690db7fdd378f37a,placeholder:"V\u00ed d\u1ee5: admin ho\u1eb7c CVHT001",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.login_username_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.login_username_rx_state_ : "")},)
  )
}


function Debounceinput_9c576e43689e3b8dc6575c3c7270c623 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_4d61c4075b9490677e993faffda368db = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_login_password", ({ ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_4d61c4075b9490677e993faffda368db,placeholder:"Nh\u1eadp m\u1eadt kh\u1ea9u",type:"password",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.login_password_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.login_password_rx_state_ : "")},)
  )
}


function Text_d04ba9f1a43444d713f8f70f819bd938 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#b91c1c", ["fontSize"] : "13px", ["fontWeight"] : "600" })},reflex___state____state__ptit_reflex___state____conduct_state.login_error_rx_state_)
  )
}


function Fragment_e5626364d644df979ec29f8b87fc0e46 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(!((reflex___state____state__ptit_reflex___state____conduct_state.login_error_rx_state_?.valueOf?.() === ""?.valueOf?.()))?(jsx(Fragment,{},jsx(Text_d04ba9f1a43444d713f8f70f819bd938,{},))):(jsx(Fragment,{},))))
  )
}


function Button_677056d91f3e1d94bcb9b96cf2702506 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_b932c69e1a6eb0360484d6d8d996b0d4 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.login", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : "#d92314", ["color"] : "white", ["border"] : "none", ["borderRadius"] : "8px", ["height"] : "44px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:on_click_b932c69e1a6eb0360484d6d8d996b0d4},"\u0110\u0103ng nh\u1eadp")
  )
}


function Debounceinput_6d3a54f3f7f1d945939bff83116ba1cd () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_ab4a8d8d55c888b9c2d25aa2248a3f39 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_register_field", ({ ["field_name"] : "register_username", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_ab4a8d8d55c888b9c2d25aa2248a3f39,placeholder:"Nh\u1eadp t\u00ean \u0111\u0103ng nh\u1eadp",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.register_username_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.register_username_rx_state_ : "")},)
  )
}


function Debounceinput_35d6b54abacb1d75c007fce77d815581 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_dfafe1245c0f4a1acf2f70e2d77393e2 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_register_field", ({ ["field_name"] : "register_full_name", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_dfafe1245c0f4a1acf2f70e2d77393e2,placeholder:"Nh\u1eadp h\u1ecd t\u00ean",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.register_full_name_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.register_full_name_rx_state_ : "")},)
  )
}


function Debounceinput_c438842fafee73e5b63b33ffdf737d8f () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_a45238ef0715bfb6e22676dd391622ec = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_register_field", ({ ["field_name"] : "register_student_code", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_a45238ef0715bfb6e22676dd391622ec,placeholder:"V\u00ed d\u1ee5: B23DCAT999",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.register_student_code_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.register_student_code_rx_state_ : "")},)
  )
}


function Debounceinput_bed799b42a62f48a2318d4f4f7760ced () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_2c95dc28fb0cdf7a3150a9d031c2e923 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_register_field", ({ ["field_name"] : "register_email", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_2c95dc28fb0cdf7a3150a9d031c2e923,placeholder:"V\u00ed d\u1ee5: tenban@stu.ptit.edu.vn",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.register_email_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.register_email_rx_state_ : "")},)
  )
}


function Debounceinput_0c823235c60201a230b3eaf2ad0dc92f () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_08b72a6f76221dcaffbf0fe915b82bb1 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_register_field", ({ ["field_name"] : "register_phone", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_08b72a6f76221dcaffbf0fe915b82bb1,placeholder:"Nh\u1eadp s\u1ed1 \u0111i\u1ec7n tho\u1ea1i",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.register_phone_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.register_phone_rx_state_ : "")},)
  )
}


function Debounceinput_f08b1677bf2c43a60dbf56e12822d83e () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_0cde6a952120e601ae459a0a567cfbc9 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_register_field", ({ ["field_name"] : "register_birth_date", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_0cde6a952120e601ae459a0a567cfbc9,placeholder:"Ch\u1ecdn ng\u00e0y sinh",type:"date",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.register_birth_date_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.register_birth_date_rx_state_ : "")},)
  )
}


function Select__root_852792c8750dd3b9cf8e8352118b49a5 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_d77aa98add7ee180c6a76aeeccbebcef = useCallback(((_ev_0) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_register_field", ({ ["field_name"] : "register_gender", ["value"] : _ev_0 }), ({  })))], [_ev_0], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesSelect.Root,{css:({ ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white", ["color"] : "#1f2937" }),onValueChange:on_change_d77aa98add7ee180c6a76aeeccbebcef,value:reflex___state____state__ptit_reflex___state____conduct_state.register_gender_rx_state_},jsx(RadixThemesSelect.Trigger,{css:({ ["width"] : "100%" })},),jsx(RadixThemesSelect.Content,{},jsx(Select__group_927e24009c346bf8c1ef212131b2d2db,{},)))
  )
}


function Debounceinput_ddcde731ffe21895e143b3213580f864 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_c75e951150728e3b47bd90c5388c73cf = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_register_field", ({ ["field_name"] : "register_class_name", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_c75e951150728e3b47bd90c5388c73cf,placeholder:"V\u00ed d\u1ee5: D23CQAT01",type:"text",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.register_class_name_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.register_class_name_rx_state_ : "")},)
  )
}


function Select__group_435a1e3eb981b101a05fc31a0ef47f1e () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesSelect.Group,{},"",Array.prototype.map.call(reflex___state____state__ptit_reflex___state____conduct_state.register_faculty_options_rx_state_ ?? [],((item_rx_state_,index_d6d6157c99650830f12a866606ea87b7)=>(jsx(RadixThemesSelect.Item,{key:index_d6d6157c99650830f12a866606ea87b7,value:item_rx_state_},item_rx_state_)))))
  )
}


function Select__root_904582f522da933b055b80a230bbc993 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_e1d33fc5d3c8b0ee67f22d1b813422bb = useCallback(((_ev_0) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_register_faculty", ({ ["value"] : _ev_0 }), ({  })))], [_ev_0], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesSelect.Root,{css:({ ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white", ["color"] : "#1f2937" }),onValueChange:on_change_e1d33fc5d3c8b0ee67f22d1b813422bb,value:reflex___state____state__ptit_reflex___state____conduct_state.register_faculty_rx_state_},jsx(RadixThemesSelect.Trigger,{css:({ ["width"] : "100%" })},),jsx(RadixThemesSelect.Content,{},jsx(Select__group_435a1e3eb981b101a05fc31a0ef47f1e,{},)))
  )
}


function Select__group_26f2cf3ce8bbc7639480316c21324f28 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(RadixThemesSelect.Group,{},"",Array.prototype.map.call(reflex___state____state__ptit_reflex___state____conduct_state.register_major_options_rx_state_ ?? [],((item_rx_state_,index_d6d6157c99650830f12a866606ea87b7)=>(jsx(RadixThemesSelect.Item,{key:index_d6d6157c99650830f12a866606ea87b7,value:item_rx_state_},item_rx_state_)))))
  )
}


function Select__root_3af518371af444ffe5f8530043b6fe6f () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_1105654fab1d8480802e6fbc457b248c = useCallback(((_ev_0) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_register_field", ({ ["field_name"] : "register_major", ["value"] : _ev_0 }), ({  })))], [_ev_0], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesSelect.Root,{css:({ ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white", ["color"] : "#1f2937" }),onValueChange:on_change_1105654fab1d8480802e6fbc457b248c,value:reflex___state____state__ptit_reflex___state____conduct_state.register_major_rx_state_},jsx(RadixThemesSelect.Trigger,{css:({ ["width"] : "100%" })},),jsx(RadixThemesSelect.Content,{},jsx(Select__group_26f2cf3ce8bbc7639480316c21324f28,{},)))
  )
}


function Debounceinput_be406e828a00086155964cb5df04e1f6 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_02c217ee482258e9981a12f6cedff08b = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_register_field", ({ ["field_name"] : "register_address", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["minHeight"] : "100px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextArea,onChange:on_change_02c217ee482258e9981a12f6cedff08b,placeholder:"Nh\u1eadp \u0111\u1ecba ch\u1ec9 hi\u1ec7n t\u1ea1i",value:reflex___state____state__ptit_reflex___state____conduct_state.register_address_rx_state_},)
  )
}


function Debounceinput_38057cd5d1cb4e4177fb0f47e5297d68 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_dda2f13b9afd7296f8b0a1f0303fd8f2 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_register_field", ({ ["field_name"] : "register_password", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_dda2f13b9afd7296f8b0a1f0303fd8f2,placeholder:"T\u1ed1i thi\u1ec3u 6 k\u00fd t\u1ef1",type:"password",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.register_password_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.register_password_rx_state_ : "")},)
  )
}


function Debounceinput_ed694a5c4b57caba9c40b165948d1163 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_cba2c9e2b0d66458cb35c6b82e396564 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.set_register_field", ({ ["field_name"] : "register_password_confirm", ["value"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["height"] : "48px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "8px", ["background"] : "white" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_cba2c9e2b0d66458cb35c6b82e396564,placeholder:"Nh\u1eadp l\u1ea1i m\u1eadt kh\u1ea9u",type:"password",value:(isNotNullOrUndefined(reflex___state____state__ptit_reflex___state____conduct_state.register_password_confirm_rx_state_) ? reflex___state____state__ptit_reflex___state____conduct_state.register_password_confirm_rx_state_ : "")},)
  )
}


function Button_e08697c1d25222380677f2c576ebecdc () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_1ebf1ac1374ff13b48d9928ad89dbbac = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.ptit_reflex___state____conduct_state.register_account", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{css:({ ["background"] : "#d92314", ["color"] : "white", ["border"] : "none", ["borderRadius"] : "8px", ["height"] : "44px", ["padding"] : "0 16px", ["fontWeight"] : "600", ["fontSize"] : "14px", ["cursor"] : (false ? "not-allowed" : "pointer"), ["opacity"] : (false ? 0.55 : 1), ["boxShadow"] : "none" }),disabled:false,onClick:on_click_1ebf1ac1374ff13b48d9928ad89dbbac},"T\u1ea1o t\u00e0i kho\u1ea3n")
  )
}


function Fragment_ee06e76072d055dc6ccff0a38e917bc1 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},((reflex___state____state__ptit_reflex___state____conduct_state.auth_mode_rx_state_?.valueOf?.() === "login"?.valueOf?.())?(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"3"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* T\u00ean \u0111\u0103ng nh\u1eadp"),jsx(Debounceinput_a303e9cf05db1f7c640ccd8f11986ccb,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* M\u1eadt kh\u1ea9u"),jsx(Debounceinput_9c576e43689e3b8dc6575c3c7270c623,{},),jsx(Fragment_e5626364d644df979ec29f8b87fc0e46,{},),jsx(Button_677056d91f3e1d94bcb9b96cf2702506,{},)))):(jsx(Fragment,{},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"3"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* T\u00ean \u0111\u0103ng nh\u1eadp"),jsx(Debounceinput_6d3a54f3f7f1d945939bff83116ba1cd,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* H\u1ecd t\u00ean"),jsx(Debounceinput_35d6b54abacb1d75c007fce77d815581,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* M\u00e3 sinh vi\u00ean"),jsx(Debounceinput_c438842fafee73e5b63b33ffdf737d8f,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* Email"),jsx(Debounceinput_bed799b42a62f48a2318d4f4f7760ced,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* S\u1ed1 \u0111i\u1ec7n tho\u1ea1i"),jsx(Debounceinput_0c823235c60201a230b3eaf2ad0dc92f,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* Ng\u00e0y sinh"),jsx(Debounceinput_f08b1677bf2c43a60dbf56e12822d83e,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* Gi\u1edbi t\u00ednh"),jsx(Select__root_852792c8750dd3b9cf8e8352118b49a5,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* L\u1edbp"),jsx(Debounceinput_ddcde731ffe21895e143b3213580f864,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* Khoa"),jsx(Select__root_904582f522da933b055b80a230bbc993,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* Ng\u00e0nh"),jsx(Select__root_3af518371af444ffe5f8530043b6fe6f,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* \u0110\u1ecba ch\u1ec9"),jsx(Debounceinput_be406e828a00086155964cb5df04e1f6,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* M\u1eadt kh\u1ea9u"),jsx(Debounceinput_38057cd5d1cb4e4177fb0f47e5297d68,{},),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["color"] : "#1f2937" })},"* X\u00e1c nh\u1eadn m\u1eadt kh\u1ea9u"),jsx(Debounceinput_ed694a5c4b57caba9c40b165948d1163,{},),jsx(Button_e08697c1d25222380677f2c576ebecdc,{},))))))
  )
}


function Fragment_596b5e10f6e6a57e212a4fdd89ae19c7 () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},((reflex___state____state__ptit_reflex___state____conduct_state.auth_mode_rx_state_?.valueOf?.() === "login"?.valueOf?.())?(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["padding"] : "14px 16px", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "10px", ["background"] : "#f8fafc" })},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "13px", ["color"] : "#1f2937", ["fontWeight"] : "700" })},"T\u00e0i kho\u1ea3n m\u1eb7c \u0111\u1ecbnh"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280" })},"Admin: admin / admin123"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280" })},"C\u1ed1 v\u1ea5n D23CQAT01: CVHT001 / CVHT001"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280" })},"C\u1ed1 v\u1ea5n D23CQAT02: CVHT002 / CVHT002"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280" })},"C\u1ed1 v\u1ea5n D23CQCN01: CVHT003 / CVHT003"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280" })},"C\u1ed1 v\u1ea5n D23CQCN02: CVHT004 / CVHT004"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "12px", ["color"] : "#6b7280" })},"Sinh vi\u00ean m\u1eabu: B23DCAT001 / B23DCAT001"))))):(jsx(Fragment,{},))))
  )
}


function Fragment_d10da9a3f9e22bbe1de40e6eb0f2863d () {
  const reflex___state____state__ptit_reflex___state____conduct_state = useContext(StateContexts.reflex___state____state__ptit_reflex___state____conduct_state)



  return (
    jsx(Fragment,{},(reflex___state____state__ptit_reflex___state____conduct_state.is_authenticated_rx_state_?(jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["height"] : "100vh", ["maxHeight"] : "100vh", ["overflow"] : "hidden", ["overflowX"] : "hidden" })},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%", ["height"] : "100vh", ["maxHeight"] : "100vh", ["background"] : "#f8fafc", ["minWidth"] : "0", ["overflow"] : "hidden" }),direction:"column",gap:"0"},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["padding"] : "10px 20px", ["background"] : "white", ["borderBottom"] : "1px solid #e5e7eb", ["flexShrink"] : "0" }),direction:"row",gap:"3"},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",direction:"row",gap:"4"},jsx("img",{alt:"PTIT",css:({ ["width"] : "58px", ["height"] : "58px", ["objectFit"] : "contain" }),src:"https://slink.ptit.edu.vn/logo.png"},),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"column",gap:"0"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},"H\u1ec6 TH\u1ed0NG \u0110\u00c1NH GI\u00c1"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["fontWeight"] : "700", ["color"] : "#1f2937", ["lineHeight"] : "1.2" })},"\u0110I\u1ec2M R\u00c8N LUY\u1ec6N"))),jsx(RadixThemesBox,{css:({ ["flex"] : "1", ["minWidth"] : "16px" })},),jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["flexWrap"] : "wrap" }),direction:"row",gap:"3"},jsx(RadixThemesBox,{css:({ ["width"] : "44px", ["height"] : "44px", ["background"] : "#c4c4c4", ["borderRadius"] : "999px", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center" })},jsx(Text_3f94262ab772c69001ae97d04536acbb,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"column",gap:"0"},jsx(Text_74cb1db8d6e4754970e3e4fb18ce7ba8,{},),jsx(Fragment_9d7fa90aa05a72acbf78a4fc85c81116,{},)),jsx(RadixThemesBox,{css:({ ["padding"] : "6px 12px", ["borderRadius"] : "999px", ["background"] : "#111827" })},jsx(Text_2351b54af388b792761e6d24fb6636ed,{},)),jsx(Button_24bda2e046077ade6297da2e52fb3438,{},))),jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%", ["flex"] : "1", ["minHeight"] : "0", ["minWidth"] : "0" }),direction:"row",gap:"0"},jsx(RadixThemesBox,{css:({ ["width"] : "272px", ["height"] : "100%", ["minHeight"] : "0", ["background"] : "white", ["borderRight"] : "1px solid #e5e7eb", ["boxShadow"] : "2px 0 5px rgba(0, 0, 0, 0.02)", ["flexShrink"] : "0", ["display"] : "flex", ["flexDirection"] : "column", ["overflowY"] : "auto" })},jsx(RadixThemesFlex,{align:"stretch",className:"rx-Stack",css:({ ["width"] : "100%", ["padding"] : "8px 10px 16px" }),direction:"column",gap:"2"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "11px", ["fontWeight"] : "700", ["color"] : "#6b7280", ["letterSpacing"] : "0.06em", ["textTransform"] : "uppercase", ["padding"] : "4px 14px 8px" })},"Menu"),jsx(Box_ccca5db63ccdc5eca9b4aabacc0f7d72,{},),jsx(Fragment_33dd63420e035ae96c5826441651aaba,{},),jsx(Fragment_0f79e807b6fa303e5172a125c10f5305,{},),jsx(Fragment_71b912e99d42d66054c6d1a1aee2d68d,{},),jsx(Fragment_cffa8700d781549bc73290504d7ec33e,{},),jsx(Fragment_a6867a429b5de75797a70aefcd2241f2,{},),jsx(Fragment_6a6c3ffcb4691f5d3d68a25a0c1dce26,{},))),jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["flex"] : "1", ["minHeight"] : "0", ["overflowY"] : "auto", ["padding"] : "24px", ["background"] : "#f8fafc", ["overflowX"] : "hidden", ["minWidth"] : "0" })},jsx(Fragment_3e2a900516bb9f51a0c09803e6005a04,{},)))),jsx(Fragment_b304926424c1a2cba1179c91f6144ff4,{},),jsx(Fragment_9238e3c2def3f8d963fefbc7b5897fe1,{},),jsx(Fragment_12ffb2a25887c9a4c43515206bb9d992,{},)))):(jsx(Fragment,{},jsx(RadixThemesFlex,{css:({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["minHeight"] : "100vh", ["width"] : "100%", ["background"] : "linear-gradient(180deg, #fff5f5 0%, #f8fafc 45%, #f1f5f9 100%)", ["padding"] : "24px" })},jsx(RadixThemesBox,{css:({ ["width"] : "100%", ["maxWidth"] : "520px", ["padding"] : "32px", ["background"] : "white", ["border"] : "1px solid #e5e7eb", ["borderRadius"] : "18px", ["boxShadow"] : "0 25px 60px rgba(15, 23, 42, 0.14)" })},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"6"},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",direction:"row",gap:"4"},jsx("img",{alt:"PTIT",css:({ ["width"] : "58px", ["height"] : "58px", ["objectFit"] : "contain" }),src:"https://slink.ptit.edu.vn/logo.png"},),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"column",gap:"0"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["fontWeight"] : "700", ["color"] : "#1f2937" })},"H\u1ec6 TH\u1ed0NG \u0110\u00c1NH GI\u00c1"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "14px", ["fontWeight"] : "700", ["color"] : "#1f2937", ["lineHeight"] : "1.2" })},"\u0110I\u1ec2M R\u00c8N LUY\u1ec6N"))),jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",direction:"column",gap:"1"},jsx(Text_7c8643a0c03f7f2d271c0eb8a31364d4,{},),jsx(Text_d22536746bf96b64b5f3cd05af99230a,{},)),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"row",gap:"3"},jsx(Button_6652e350c055b10465602d6ca2cedcd5,{},),jsx(Button_f2e9d294f6ffe21813037a6ceeac1a50,{},)),jsx(Fragment_ace4f9daeb0704d294dde9e1d0d362fd,{},),jsx(Fragment_ee06e76072d055dc6ccff0a38e917bc1,{},),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"3"},jsx(Fragment_596b5e10f6e6a57e212a4fdd89ae19c7,{},)))))))))
  )
}


export default function Component() {





  return (
    jsx(Fragment,{},jsx(Fragment_d10da9a3f9e22bbe1de40e6eb0f2863d,{},),jsx("title",{},"H\u1ec7 th\u1ed1ng \u0111\u00e1nh gi\u00e1 \u0111i\u1ec3m r\u00e8n luy\u1ec7n"),jsx("meta",{content:"favicon.ico",property:"og:image"},))
  )
}