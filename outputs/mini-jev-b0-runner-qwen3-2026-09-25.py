#!/usr/bin/env python3
"""W5 B0 rerun, qwen3:4b, think ON (default). think=false breaks instruction
following on this Ollama build (model echoes prompt). 30 cases x 77 labels x 3.
Incremental save to outputs/ (survives timeouts). Usage: b0_run_q3.py [from to]"""
import json
import sys
import time
import urllib.request
from collections import Counter

HOSTS = ["http://192.168.1.209:11434", "http://10.24.175.30:11434"]
MODEL = "qwen3:4b"
RUNS = 3
OUTP = "/Users/victor/Projects/ai-qa-wiki/outputs/mini-jev-b0-qwen3-4b-raw-2026-09-25.json"

LABELS = ["Age_limit", "Apple_pay_or_google_pay", "Atm_support", "Balance_not_updated_after_bank_transfer", "Balance_not_updated_after_cheque_or_cash_deposit", "Beneficiary_not_allowed", "Cancel_transfer", "Card_about_to_expire", "Card_acceptance", "Card_arrival", "Card_delivery_estimate", "Card_linking", "Card_not_working", "Card_payment_fee_charged", "Card_payment_not_recognised", "Card_payment_wrong_exchange_rate", "Card_swallowed", "Cash_withdrawal_charge", "Cash_withdrawal_not_recognised_as_cash", "Change_pin", "Compromised_card", "Contactless_not_working", "Country_support", "Declined_card_payment", "Declined_cash_withdrawal", "Declined_transfer", "Direct_debit_payment_not_recognised", "Disposable_card_limits", "Edit_personal_details", "Exchange_charge", "Exchange_rate", "Exchange_via_app", "Extra_charge_on_statement", "Failed_transfer", "Fiat_currency_support", "Get_disposable_virtual_card", "Get_physical_card", "Getting_spare_card", "Getting_virtual_card", "Lost_or_stolen_card", "Lost_or_stolen_phone", "Order_physical_card", "Passcode_forgotten", "Pending_card_payment", "Pending_cash_withdrawal", "Pending_top_up", "Pending_transfer", "Pin_blocked", "Receiving_money", "Refund_not_showing_up", "Report_fraud", "Request_refund", "Reverted_card_payment?", "Review_ongoing", "Supported_cards_and_currencies", "Terminate_account", "Top_up_by_bank_transfer_charge", "Top_up_by_card_charge", "Top_up_by_cash_or_cheque", "Top_up_failed", "Top_up_limits", "Top_up_reverted", "Topping_up_by_card", "Transaction_charged_twice", "Transfer_fee_charged", "Transfer_into_account", "Transfer_not_received_by_recipient", "Transfer_timing", "Unable_to_verify_identity", "Verify_my_identity", "Verify_source_of_funds", "Verify_top_up", "Virtual_card_not_working", "Visa_or_mastercard", "Why_verify_identity", "Wrong_amount_of_cash_received", "Wrong_exchange_rate_for_cash_withdrawal"]
LOWER = {l.lower(): l for l in LABELS}

CASES = [
    ("B0-01", "The refund isn't showing up on my account.", "Refund_not_showing_up"),
    ("B0-02", "I would like to have a new card because I lost mine.", "Lost_or_stolen_card"),
    ("B0-03", "My card is not working for contactless payments.", "Contactless_not_working"),
    ("B0-04", "How long will it take for my transfer to arrive?", "Transfer_timing"),
    ("B0-05", "I was charged twice for the same transaction.", "Transaction_charged_twice"),
    ("B0-06", "What is the exchange rate for dollars?", "Exchange_rate"),
    ("B0-07", "I forgot my passcode, how do I reset it?", "Passcode_forgotten"),
    ("B0-08", "Someone used my card without permission.", "Report_fraud"),
    ("B0-09", "Why was my card declined?", "Declined_card_payment"),
    ("B0-10", "How do I top up using my bank?", "Top_up_by_bank_transfer_charge"),
    ("B0-11", "My PIN is blocked, what should I do?", "Pin_blocked"),
    ("B0-12", "Can I get a virtual card?", "Get_disposable_virtual_card"),
    ("B0-13", "A payment is pending on my card, what does that mean?", "Pending_card_payment"),
    ("B0-14", "How do I change my PIN?", "Change_pin"),
    ("B0-15", "My card was swallowed by the ATM.", "Card_swallowed"),
    ("B0-16", "Is there a fee for card payments abroad?", "Card_payment_fee_charged"),
    ("B0-17", "I want to cancel a transfer I just made.", "Cancel_transfer"),
    ("B0-18", "How do I verify my identity?", "Verify_my_identity"),
    ("B0-19", "My top up failed, why?", "Top_up_failed"),
    ("B0-20", "What currencies do you support?", "Fiat_currency_support"),
    ("B0-21", "I need to update my personal details.", "Edit_personal_details"),
    ("B0-22", "There is an extra charge on my statement I don't recognise.", "Extra_charge_on_statement"),
    ("B0-23", "How do I get a new physical card?", "Order_physical_card"),
    ("B0-24", "Can I use Apple Pay?", "Apple_pay_or_google_pay"),
    ("B0-25", "My transfer failed.", "Failed_transfer"),
    ("B0-26", "Which countries do you support?", "Country_support"),
    ("B0-27", "I lost my phone, what do I do about my account?", "Lost_or_stolen_phone"),
    ("B0-28", "How do I close my account?", "Terminate_account"),
    ("B0-29", "Someone received my transfer? No - I want to know if my transfer arrived.", "Transfer_not_received_by_recipient"),
    ("B0-30", "Why do you require so many details about my identity?", "why_verify_identity"),
]

PROMPT = ("Classify this customer message into EXACTLY ONE of the 77 labels below. "
          "Reply with only the exact label text, nothing else.\nLabels: {labels}\nMessage: {text}\nLabel:")


def api(host, payload, timeout=600):
    req = urllib.request.Request(
        host + "/api/generate",
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def pick_host():
    for h in HOSTS:
        try:
            urllib.request.urlopen(h + "/", timeout=5)
            return h
        except Exception:
            continue
    raise RuntimeError("no Ollama reachable")


def main():
    lo = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    hi = int(sys.argv[2]) if len(sys.argv) > 2 else len(CASES)
    host = pick_host()
    print(f"host={host} model={MODEL} slice=[{lo}:{hi}]", flush=True)
    rows = []
    t0 = time.time()
    for cid, text, gold in CASES[lo:hi]:
        for run in range(1, RUNS + 1):
            t1 = time.time()
            try:
                r = api(host, {"model": MODEL,
                               "prompt": PROMPT.format(labels=", ".join(LABELS), text=text),
                               "stream": False,
                               "options": {"temperature": 0}})
                lat = time.time() - t1
                lines = [ln.strip().strip(" \"'") for ln in r.get("response", "").strip().splitlines() if ln.strip()]
                got = lines[-1] if lines else ""
                hit = LOWER.get(got.lower())
                if hit and hit.lower() == gold.lower():
                    verdict = "HIT"
                elif hit:
                    verdict = "MISS->" + hit
                else:
                    verdict = "UNPARSEABLE"
            except Exception as e:
                lat = time.time() - t1
                got = ""
                verdict = "ERROR:" + str(e)[:50]
            rows.append({"id": cid, "run": run, "latency_s": round(lat, 2),
                         "got": got[:80], "gold": gold, "verdict": verdict})
            print(rows[-1], flush=True)
            with open(OUTP, "w") as f:
                json.dump({"partial": True, "model": MODEL, "rows": rows}, f, indent=1)
    total = time.time() - t0
    hits = sum(1 for r in rows if r["verdict"] == "HIT")
    print(f"SLICE [{lo}:{hi}]: {len(rows)} calls in {round(total, 1)}s | acc {hits}/{len(rows)}", flush=True)
    with open(OUTP, "w") as f:
        json.dump({"model": MODEL, "method": "generative 1-of-77 judge, temp 0, think ON, case-insensitive scoring",
                   "batch_s": round(total, 1), "accuracy": f"{hits}/{len(rows)}", "rows": rows}, f, indent=1)


if __name__ == "__main__":
    main()
