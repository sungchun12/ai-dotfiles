#!/usr/bin/env python3
"""
Simple pydantic-ai agent example.

Demonstrates:
- Type-safe tool definitions
- Structured output with Pydantic models
- Mixing AI calls with deterministic code

Usage:
    export ANTHROPIC_API_KEY="your-key"
    python simple_agent.py "Analyze the sales data for Q4"

Requirements:
    pip install pydantic-ai
"""
from __future__ import annotations

import sys
from datetime import datetime
from typing import Literal

from pydantic import BaseModel
from pydantic_ai import Agent, RunContext


# --- Output Models ---

class AnalysisResult(BaseModel):
    """Structured output from the analysis agent."""

    summary: str
    confidence: Literal["high", "medium", "low"]
    key_findings: list[str]
    recommended_actions: list[str]


# --- Tool Context ---

class AnalysisContext(BaseModel):
    """Context passed to tools."""

    user_query: str
    timestamp: datetime


# --- Tools ---

def get_sample_data(ctx: RunContext[AnalysisContext]) -> dict:
    """Fetch sample data for analysis.

    In a real agent, this would query a database or API.
    """
    return {
        "q4_sales": 1_250_000,
        "q3_sales": 980_000,
        "growth_rate": 0.276,
        "top_products": ["Widget A", "Gadget B", "Service C"],
        "regions": {"North": 450_000, "South": 320_000, "East": 280_000, "West": 200_000},
    }


def calculate_trend(ctx: RunContext[AnalysisContext], values: list[float]) -> str:
    """Calculate trend direction from a series of values."""
    if len(values) < 2:
        return "insufficient_data"

    diff = values[-1] - values[0]
    if diff > 0:
        return "increasing"
    elif diff < 0:
        return "decreasing"
    return "stable"


# --- Agent Definition ---

analysis_agent = Agent(
    "claude-3-5-sonnet-latest",
    deps_type=AnalysisContext,
    result_type=AnalysisResult,
    system_prompt="""You are a data analyst assistant.

When asked to analyze data:
1. Use the get_sample_data tool to fetch relevant data
2. Use calculate_trend for trend analysis
3. Provide structured findings with actionable recommendations
4. Be specific and quantitative in your analysis
""",
)

# Register tools
analysis_agent.tool(get_sample_data)
analysis_agent.tool(calculate_trend)


# --- Main ---

async def main(query: str) -> AnalysisResult:
    """Run the analysis agent with a query."""
    context = AnalysisContext(
        user_query=query,
        timestamp=datetime.now(),
    )

    result = await analysis_agent.run(query, deps=context)
    return result.data


if __name__ == "__main__":
    import asyncio

    if len(sys.argv) < 2:
        print("Usage: python simple_agent.py 'your query'")
        sys.exit(1)

    query = sys.argv[1]
    result = asyncio.run(main(query))

    print(f"\n{'='*50}")
    print(f"Summary: {result.summary}")
    print(f"Confidence: {result.confidence}")
    print(f"\nKey Findings:")
    for finding in result.key_findings:
        print(f"  - {finding}")
    print(f"\nRecommended Actions:")
    for action in result.recommended_actions:
        print(f"  - {action}")
