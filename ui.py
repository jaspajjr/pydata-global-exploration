import os

import httpx
import streamlit as st

API_BASE = os.getenv("API_BASE", "http://localhost:8000")


def api_get(path: str):
    try:
        r = httpx.get(f"{API_BASE}{path}")
        r.raise_for_status()
        return r.json()
    except httpx.ConnectError:
        st.error("Cannot connect to the API. Is `fastapi dev main.py` running on :8000?")
        return None
    except httpx.HTTPStatusError as e:
        st.error(f"API error: {e.response.text}")
        return None


def api_post(path: str, data: dict):
    try:
        r = httpx.post(f"{API_BASE}{path}", json=data)
        r.raise_for_status()
        return r.json()
    except httpx.ConnectError:
        st.error("Cannot connect to the API.")
        return None
    except httpx.HTTPStatusError as e:
        st.error(f"API error: {e.response.text}")
        return None


def api_put(path: str, data: dict):
    try:
        r = httpx.put(f"{API_BASE}{path}", json=data)
        r.raise_for_status()
        return r.json()
    except httpx.ConnectError:
        st.error("Cannot connect to the API.")
        return None
    except httpx.HTTPStatusError as e:
        st.error(f"API error: {e.response.text}")
        return None


def api_delete(path: str):
    try:
        r = httpx.delete(f"{API_BASE}{path}")
        r.raise_for_status()
        return True
    except httpx.ConnectError:
        st.error("Cannot connect to the API.")
        return False
    except httpx.HTTPStatusError as e:
        st.error(f"API error: {e.response.text}")
        return False


st.title("PyData Global Registry")

organiser_tab, meetup_tab = st.tabs(["Organisers", "Meetups"])

# ── Organisers ──────────────────────────────────────────────────────────────

with organiser_tab:
    st.subheader("All Organisers")
    organisers = api_get("/organisers") or []
    if organisers:
        st.dataframe(organisers, use_container_width=True)
    else:
        st.info("No organisers yet.")

    action = st.radio("Action", ["Add", "Edit", "Delete"], horizontal=True, key="org_action")

    if action == "Add":
        with st.form("add_organiser"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            linkedin = st.text_input("LinkedIn URL")
            photo = st.text_input("Photo URL")
            if st.form_submit_button("Create"):
                result = api_post("/organisers", {
                    "name": name,
                    "email": email,
                    "linkedin": linkedin,
                    "photo": photo,
                })
                if result:
                    st.success(f"Organiser '{name}' created.")
                    st.rerun()

    elif action == "Edit":
        if not organisers:
            st.info("No organisers to edit.")
        else:
            by_id = {o["organiser_id"]: o for o in organisers}
            selected_id = st.selectbox("Select organiser", list(by_id), key="org_edit_select")
            current = by_id[selected_id]
            with st.form("edit_organiser"):
                name = st.text_input("Name", value=current["name"])
                email = st.text_input("Email", value=current["email"])
                linkedin = st.text_input("LinkedIn URL", value=current["linkedin"])
                photo = st.text_input("Photo URL", value=current["photo"])
                if st.form_submit_button("Save"):
                    result = api_put(f"/organisers/{selected_id}", {
                        "organiser_id": selected_id,
                        "name": name,
                        "email": email,
                        "linkedin": linkedin,
                        "photo": photo,
                    })
                    if result:
                        st.success("Organiser updated.")
                        st.rerun()

    elif action == "Delete":
        if not organisers:
            st.info("No organisers to delete.")
        else:
            selected_id = st.selectbox(
                "Select organiser to delete",
                [o["organiser_id"] for o in organisers],
                key="org_delete_select",
            )
            if st.button("Delete", type="primary", key="org_delete_btn"):
                if api_delete(f"/organisers/{selected_id}"):
                    st.success(f"Organiser '{selected_id}' deleted.")
                    st.rerun()

# ── Meetups ──────────────────────────────────────────────────────────────────

with meetup_tab:
    st.subheader("All Meetups")
    meetups = api_get("/meetups") or []
    if meetups:
        st.dataframe(meetups, use_container_width=True)
    else:
        st.info("No meetups yet.")

    action = st.radio("Action", ["Add", "Edit", "Delete"], horizontal=True, key="meetup_action")

    if action == "Add":
        with st.form("add_meetup"):
            name = st.text_input("Name")
            city = st.text_input("City")
            chapter_email = st.text_input("Chapter Email")
            google_group = st.text_input("Google Group")
            organisers_input = st.text_input("Organiser IDs (comma-separated)")
            if st.form_submit_button("Create"):
                result = api_post("/meetups", {
                    "name": name,
                    "city": city,
                    "chapter_email": chapter_email,
                    "google_group": google_group,
                    "organisers": [o.strip() for o in organisers_input.split(",") if o.strip()],
                })
                if result:
                    st.success(f"Meetup '{name}' created.")
                    st.rerun()

    elif action == "Edit":
        if not meetups:
            st.info("No meetups to edit.")
        else:
            by_id = {m["meetup_id"]: m for m in meetups}
            selected_id = st.selectbox("Select meetup", list(by_id), key="meetup_edit_select")
            current = by_id[selected_id]
            with st.form("edit_meetup"):
                name = st.text_input("Name", value=current["name"])
                city = st.text_input("City", value=current["city"])
                chapter_email = st.text_input("Chapter Email", value=current["chapter_email"])
                google_group = st.text_input("Google Group", value=current["google_group"])
                organisers_input = st.text_input(
                    "Organiser IDs (comma-separated)",
                    value=", ".join(current["organisers"]),
                )
                if st.form_submit_button("Save"):
                    result = api_put(f"/meetups/{selected_id}", {
                        "meetup_id": selected_id,
                        "name": name,
                        "city": city,
                        "chapter_email": chapter_email,
                        "google_group": google_group,
                        "organisers": [o.strip() for o in organisers_input.split(",") if o.strip()],
                    })
                    if result:
                        st.success("Meetup updated.")
                        st.rerun()

    elif action == "Delete":
        if not meetups:
            st.info("No meetups to delete.")
        else:
            selected_id = st.selectbox(
                "Select meetup to delete",
                [m["meetup_id"] for m in meetups],
                key="meetup_delete_select",
            )
            if st.button("Delete", type="primary", key="meetup_delete_btn"):
                if api_delete(f"/meetups/{selected_id}"):
                    st.success(f"Meetup '{selected_id}' deleted.")
                    st.rerun()
