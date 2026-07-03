"""
The cognitive loop
The cognitive architecture of intelligent agents defines how perception transforms into purposeful action
through structured, repeatable processes. At the heart of this design lies the cognitive loop, a continuous cycle
of perception, reasoning, planning, action, and learning, which enables agents to operate autonomously in
dynamic environments. As illustrated in Figure 1.2, this loop forms the backbone of intelligent agent behavior,
providing the scaffolding through which decisions are made, actions are executed, and knowledge is
accumulated over time

To understand how this architecture functions in practice, let's explore each phase of the cognitive loop in
detail, beginning with perception, which is the critical first step that shapes everything that as follows:"""

"""Perception initiates the loop by capturing data from the environment, whether through user input,
APIs, sensors, or external systems, and converting it into structured formats suitable for processing.
This raw input forms the basis for subsequent cognitive steps and determines the scope of the agent's
situational awareness. """

def perceive_user_input(user_message, context):
    return {
        "message": user_message, 
        "timestamp": datetime.now(), 
        "user_id": context.get("user_id"), 
        "session_state": context.get("session"),
        "sentiment": analyze_sentiment(user_message)
    }
"""
Reasoning follows idx_c45c48fcby contextualizing this perceived information, applying pattern recognition,
inference engines, or statistical models to extract meaning and relevance. This stage transforms signals
into insights, allowing the agent to understand not just what is happening, but why it matters.
"""
def reason_about_intent(perception_data):
    intent = classify_intent(percenption_data["message"])
    priority = determine_priority(
        intent,
        perception_data['sentiment'], 
        user_history = get_user_history(perception_data['user_id'])
    )
    return{'intent': intent, 
           'priority': priority, 
           'context': perception_data 
    }}

"""Planning orchestrates idx_9e69e7a1these insights into a coherent sequence of actions. Whether using deterministic
rule chains or probabilistic models, the agent decomposes objectives into tasks, evaluates options, and
prioritizes steps in accordance with predefined goals and environmental conditions.
"""
def create_action_plan(reasoning_result):
    if reasoning_result["intent"]== "billing_issue":
        return[
            "fetch_account_details", 
            "analyze_billing_history", 
            "generate_explanation", 
            "offer_resolution"
        ]
    elif reasoning_result["priority"]=="urgent":
        return ["escalate_to_human", "log_urgent_case"]
    
"""
Action thenidx_6438da9c executes the selected steps, interfacing idx_5b4f8ab2with external tools, APIs, databases, or systems to
operationalize the agent's decisions. This phase is often implemented using function-calling
frameworks or tool orchestration layers such as those found in LangChain or LangGraph.
"""

def execute_action(action_plan, context):
    result =[]

    for action in action_plan:
        if action == "fetch_account_details":
            result = billing_api.get_account(context["user_id"])
        elif action == "generate_explanation":
            result = llm.generate_response(context, result)
        result.append(result)
    return results

"""Learning closes theidx_d24eb2bc loop by analyzing outcomes, measuring the success of actions, and updating
internal models or memory stores. This feedback mechanism allows the agent to refine its behavior over
time, improving performance based on both successes and failures."""

def learn_from_outcome(interaction_data, user_feedback):
    success_score = calculate_success(user_feedback)
    update_user_preferences(interaction_data["user_id"], success_score)
    if success_score < 0.7:
        flag_for_model_improvement(interaction_data)



