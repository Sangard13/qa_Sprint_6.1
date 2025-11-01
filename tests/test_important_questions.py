import pytest
import allure
from pages.main_page import MainPage
from data import FAQ_DATA


class TestImportantQuestions:

    @allure.title("Проверка ответов на вопросы в разделе 'Вопросы о важном'")
    @pytest.mark.parametrize("question_index,expected_answer", FAQ_DATA)
    def test_question_reveals_correct_answer(self, driver, question_index, expected_answer):
        main_page = MainPage(driver)
        main_page.open_main_page()

        main_page.click_question(question_index)
        actual_answer = main_page.get_answer_text(question_index)

        assert actual_answer == expected_answer