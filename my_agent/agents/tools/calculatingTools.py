from datetime import datetime
from google.adk.tools.tool_context import ToolContext

def get_system_datetime(context: ToolContext) -> str:
    """Returns the current date, time, and day of the week."""
    
    now = datetime.now()
    formatted_data = now.strftime("%Y-%m-%d %H:%M:%S (%A)")
    context.state["last_checked_datetime"] = formatted_data
    return formatted_data
import os


def save_quick_note(title: str, content: str, context: ToolContext) -> str:
    """Saves a quick note to a local text file.

    Args:
        title: The title/filename for the note (without extension).
        content: The text body to save into the file.
    """
    notes_dir = "agent_notes"
    os.makedirs(notes_dir, exist_ok=True)

    file_path = os.path.join(notes_dir, f"{title}.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    saved_notes= context.state.get("saved_notes", [])
    saved_notes.append({"title": title, "content": content, "file_path": file_path})
    context.state["saved_notes"] = saved_notes
    context.state["temp:last_saved_note"] =title
    
    return f"Note successfully saved to {file_path}"

def get_simulated_fx_rate(from_currency: str, to_currency: str, context: ToolContext) -> str:
    """Provides indicative exchange rates between common currencies.

    Args:
        from_currency: The base currency code (e.g., 'USD', 'EUR', 'TRY').
        to_currency: The target currency code (e.g., 'USD', 'EUR', 'TRY').
    """
    rates_to_usd = {"USD": 1.0, "EUR": 1.08, "TRY": 0.029, "GBP": 1.28}

    base = from_currency.upper()
    target = to_currency.upper()

    if base not in rates_to_usd or target not in rates_to_usd:
        return f"Unsupported currency pair: {base} to {target}"

    rate = rates_to_usd[base] / rates_to_usd[target]
    last_rate_info= context.state.get("last_fx_rate_info", [])
    last_rate_info.append({"from_currency": base, "to_currency": target, "rate": rate})
    context.state["last_rate_info"] = last_rate_info
    context.state["temp:last_fx_rate"] = f"1 {base} = {rate:.4f} {target}"
    
    return f"1 {base} = {rate:.4f} {target}"