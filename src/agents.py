from .llm import generate_response


def research_agent(
    company,
    industry,
    website,
    description
):

    prompt = f"""
Analyze this company as a B2B AI lead.

Company: {company}
Industry: {industry}
Website: {website}
Description: {description}

Provide:

1. Company summary
2. Potential AI use cases
3. Business problems
4. Automation opportunities
5. Ideal decision maker
6. Why this company could be a potential customer

Keep the response concise and practical.
"""

    return generate_response(
        "You are an expert B2B AI lead researcher.",
        prompt
    )


def scoring_agent(
    company,
    industry,
    description
):

    prompt = f"""
Evaluate this company as a potential AI customer.

Company: {company}
Industry: {industry}
Description: {description}

Evaluate:

- AI Fit
- Business Potential
- Automation Opportunity
- Customer Acquisition Potential

Give each score from 0-100.

Then provide an overall lead score from 0-100.

Explain the reasoning.
"""

    return generate_response(
        "You are an expert B2B lead qualification agent.",
        prompt
    )


def outreach_agent(
    company,
    industry,
    problem
):

    prompt = f"""
Create a personalized B2B outreach message.

Company: {company}
Industry: {industry}
Potential Problem: {problem}

Requirements:

- Less than 120 words
- Professional
- Personalized
- No spammy language
- Mention the potential problem
- Explain how AI can help
- Include a simple call to action

Return only the message.
"""

    return generate_response(
        "You are an expert B2B outreach copywriter.",
        prompt
    )