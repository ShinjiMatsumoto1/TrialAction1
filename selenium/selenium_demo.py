import os
import datetime
import time
import inspect
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

# web driver の設定と読み込み
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options) 
# window 最大で起動
driver.maximize_window()

TARGET_PAGE = 'https://aig-tri-sqa-web.sssiotpfs.com/'
OUTPUT_CAPTURE = 'capture\\'
OUTPUT_LOG = 'log\\'

# x path 
sign_in_button_x_path = "/html/body/app-root/ng-component/app-header/nav/div[2]/div[3]/cmn-button[1]/button"
sign_up_button_x_path = "/html/body/app-root/ng-component/app-header/nav/div[2]/div[3]/cmn-button[2]/button"
address_x_path = "/html/body/app-root/ng-component/mat-sidenav-container/mat-sidenav-content/div/app-create-user/div/div/div/form/table/tbody/tr[1]/td/div/cmn-input-form/div/div/cmn-input/div/input"
sei_x_path = "/html/body/app-root/ng-component/mat-sidenav-container/mat-sidenav-content/div/app-create-user/div/div/div/form/table/tbody/tr[2]/td/div/div/cmn-input-form[1]/div/div/cmn-input/div/input"
name_x_path = "/html/body/app-root/ng-component/mat-sidenav-container/mat-sidenav-content/div/app-create-user/div/div/div/form/table/tbody/tr[2]/td/div/div/cmn-input-form[2]/div/div/cmn-input/div/input"
language_x_path = "/html/body/app-root/ng-component/mat-sidenav-container/mat-sidenav-content/div/app-create-user/div/div/div/form/table/tbody/tr[3]/td/div/cmn-selectbox-form/div/cmn-selectbox/div/select"
check_user_x_path = "/html/body/app-root/ng-component/mat-sidenav-container/mat-sidenav-content/div/app-create-user/div/div/div/form/table/tbody/tr[4]/td/div/cmn-button[1]/button"
check_user_daialog_x_path = '//*[@id="mat-dialog-0"]/cmn-terms-dialog/div/div[2]/div/div/cmn-service-term/div/ol[8]/li[5]'
check_user_daialog_close_x_path = '//*[@id="mat-dialog-0"]/cmn-terms-dialog/div/div[1]/button/mat-icon'
check_privacy_x_path = "/html/body/app-root/ng-component/mat-sidenav-container/mat-sidenav-content/div/app-create-user/div/div/div/form/table/tbody/tr[4]/td/div/cmn-button[2]/button"
check_privacy_daialog_x_path = '//*[@id="mat-dialog-1"]/cmn-terms-dialog/div/div[2]/div/div/cmn-privacy-policy/div/strong'
check_privacy_daialog_close_x_path = '//*[@id="mat-dialog-1"]/cmn-terms-dialog/div/div[1]/button/mat-icon'
doui_x_path = '/html/body/app-root/ng-component/mat-sidenav-container/mat-sidenav-content/div/app-create-user/div/div/div/form/table/tbody/tr[6]/td/div/cmn-checkbox-form/div/cmn-checkbox/label/input'
touroku_x_path = '/html/body/app-root/ng-component/mat-sidenav-container/mat-sidenav-content/div/app-create-user/div/div/div/form/table/tbody/tr[7]/td/div/cmn-button/button'

def open_browser():
    driver.get( TARGET_PAGE )

def close_browser():
    driver.quit()

def capture( output_directory ):
    width = driver.execute_script('return document.body.scrollWidth;')
    height = driver.execute_script('return document.body.scrollHeight;')
    driver.set_window_size(width, height)
    output_directory = output_directory + '\\'
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    file_name = output_directory + str( now.strftime('%Y%m%d%H%M%S') ) + '.png'
    driver.save_screenshot(file_name)

def create_capture_directory( capture_directory ):
    capture_abs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), capture_directory )
    os.makedirs( capture_abs_dir, exist_ok=True )

    return capture_abs_dir

def input_user_info( address, sei, name, language ):
    input_address = driver.find_element_by_xpath(address_x_path)
    input_address.send_keys(address)
    input_sei = driver.find_element_by_xpath(sei_x_path)
    input_sei.send_keys(sei)
    input_name = driver.find_element_by_xpath(name_x_path)
    input_name.send_keys(name)
    input_language = driver.find_element_by_xpath(language_x_path)
    Select(input_language).select_by_value(language)

def click( click_contents ):
    click_button = driver.find_element_by_xpath( click_contents )
    click_button.click()

def scroll_daialog( scroll_contents ):
    last_element = driver.find_element_by_xpath( scroll_contents )
    driver.execute_script("arguments[0].scrollIntoView(true);", last_element)

def case_N_N_N():
    name_method = inspect.currentframe().f_code.co_name
    capture_dir = OUTPUT_CAPTURE + name_method
    caputure_abs_directory = create_capture_directory( capture_dir )
    # operation start
    # AITORIUSにアクセス
    open_browser()
    time.sleep(3)
    capture( caputure_abs_directory )
    # sign_upボタン押下
    click( sign_up_button_x_path )
    time.sleep(3)
    capture( caputure_abs_directory )
    # ユーザー情報入力
    input_user_info(address = 'gcs_test@sony.com',
                    sei = '田中',
                    name = '太郎',
                    language = 'ja')
    time.sleep(3)
    capture( caputure_abs_directory )
    # ユーザー登録規約確認押下
    click( check_user_x_path )
    time.sleep(3)
    capture( caputure_abs_directory )
    # ユーザー登録規約スクロール
    scroll_daialog( check_user_daialog_x_path )
    time.sleep(3)
    capture( caputure_abs_directory )
    # ユーザー登録規約閉じる
    click( check_user_daialog_close_x_path )
    time.sleep(3)
    capture( caputure_abs_directory )
    # プライバシーポリシー押下
    click( check_privacy_x_path )
    time.sleep(3)
    capture( caputure_abs_directory )
    # プライバシーポリシースクロール
    scroll_daialog( check_privacy_daialog_x_path )
    time.sleep(3)
    capture( caputure_abs_directory )
    # プライバシーポリシー閉じる
    click( check_privacy_daialog_close_x_path )
    time.sleep(5)
    capture( caputure_abs_directory )
    # 同意にチェック
    click( doui_x_path )
    capture( caputure_abs_directory )

    # 登録ボタン押下
    #click( touroku_x_path )
    #capture( caputure_abs_directory )

    close_browser()

if __name__ == "__main__":
    # call test case
    case_N_N_N()
