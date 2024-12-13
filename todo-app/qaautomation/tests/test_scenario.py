import pytest
from playwright.sync_api import expect


def test_add_task(page):
    page.get_by_text("Add Task").click()

    page.wait_for_selector('div[class^="modal_wrapper__"]', state="visible")
    modal = page.locator('div[class^="modal_wrapper__"]')

    modal.locator("input#title").fill("Test 1")
    modal.locator("button[type='submit']").click()


    page.wait_for_selector("div[role='status']:has-text('Task added successfully')", state="visible")
    expect(page.locator('p[class^="todoItem"][class$="false"]')).to_have_text("Test 1")

def test_update_task(page):
    page.get_by_text("Add Task").click()

    page.wait_for_selector('div[class^="modal_wrapper__"]', state="visible")
    modal = page.locator('div[class^="modal_wrapper__"]')

    modal.locator("input#title").fill("Test 2")
    modal.locator("button[type='submit']").click()

    page.locator('div[class^="todoItem_icon__"]').nth(1).click()
    modal.locator("input#title").fill("")
    modal.locator("button[type='submit']").click()

    page.wait_for_selector("div[role='status']:has-text('Please enter a title')", state="visible")
    modal.locator("input#title").fill("Test 3")
    modal.locator("select[id='type']").select_option("Completed")

    modal.locator("button[type='submit']").click()


    page.wait_for_selector("div[role='status']:has-text('Task Updated successfully')", state="visible")

def test_delete_task(page):
    page.get_by_text("Add Task").click()

    page.wait_for_selector('div[class^="modal_wrapper__"]', state="visible")
    modal = page.locator('div[class^="modal_wrapper__"]')

    modal.locator("input#title").fill("Test 1")
    modal.locator("button[type='submit']").click()
    page.locator('div[class^="todoItem_icon__"]').nth(0).click()


    page.wait_for_selector("div[role='status']:has-text('Todo Deleted Successfully')", state="visible")
    expect(page.locator('div[class^="todoItem_item__"]')).to_have_count(0)


def test_change_task_status(page):
    page.get_by_text("Add Task").click()

    page.wait_for_selector('div[class^="modal_wrapper__"]', state="visible")
    modal = page.locator('div[class^="modal_wrapper__"]')

    modal.locator("input#title").fill("Test 4")
    modal.locator("button[type='submit']").click()


    page.locator('div[class^="todoItem_svgBox__"]').click()
    expect(page.locator('p[class^="todoItem"][class*="completed"]')).to_have_text("Test 4")

    page.locator('div[class^="todoItem_svgBox__"]').click()
    expect(page.locator('p[class^="todoItem"][class$="false"]')).to_have_text("Test 4")


def test_filter_tasks(page):
    page.get_by_text("Add Task").click()
    page.wait_for_selector('div[class^="modal_wrapper__"]', state="visible")
    modal = page.locator('div[class^="modal_wrapper__"]')
    modal.locator("input#title").fill("Test 5")
    modal.locator("button[type='submit']").click()

    page.wait_for_timeout(700)

    page.get_by_text("Add Task").click()
    page.wait_for_selector('div[class^="modal_wrapper__"]', state="visible")
    modal = page.locator('div[class^="modal_wrapper__"]')
    modal.locator("input#title").fill("Test 6")
    modal.locator("button[type='submit']").click()

    page.locator('div[class^="todoItem_svgBox__"]').nth(0).click()


    page.locator("select[id='status']").select_option("Completed")
    expect(page.locator('div[class^="todoItem_item__"]')).to_have_count(1)

    page.locator("select[id='status']").select_option("Incomplete")
    expect(page.locator('div[class^="todoItem_item__"]')).to_have_count(1)

    page.locator("select[id='status']").select_option("All")
    expect(page.locator('div[class^="todoItem_item__"]')).to_have_count(2)