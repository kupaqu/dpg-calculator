import dearpygui.dearpygui as dpg
import numexpr as ne

def click_callback(sender, app_data, user_data):
    lbl = dpg.get_item_label(sender)
    expression = dpg.get_value(entry)

    if lbl == "C":
        dpg.set_value(entry, '')

    elif lbl == "=":

        try:
            evaluated = ne.evaluate(expression)

            # https://docs.python.org/3/tutorial/floatingpoint.html
            if evaluated.dtype == 'float':
                evaluated = round(float(evaluated), 10)
                
            dpg.set_value(entry, evaluated)

        except SyntaxError:
            dpg.set_value(entry, "Syntax error! Clear to continue!")

        except ZeroDivisionError:
            dpg.set_value(entry, "Zero division error! Clear to continue!")
            
    else:
        dpg.set_value(entry, expression+lbl)

dpg.create_context()
dpg.create_viewport(title='DearPyGUI Calculator', width=400, height=400)

with dpg.window(tag='Primary Window', label='Calculator', no_resize=True, no_close=True, width=400, height=400):
    entry = dpg.add_input_text(tag='Entry')
    dpg.set_item_width(entry, dpg.get_viewport_client_width())
    labels = ['123+', '456-', '789*', 'C0=/']
    for i in range(1, 5):
        with dpg.group(horizontal=True):
            for j in range(4):
                print(i, j)
                btn_lbl = labels[i-1][j]
                btn = dpg.add_button(label=btn_lbl, tag='Btn'+btn_lbl)
                dpg.set_item_width(btn, 50)
                dpg.set_item_height(btn, 50)
                dpg.set_item_callback(btn, click_callback)
                dpg.set_item_user_data(btn, entry)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window('Primary Window', True)
dpg.start_dearpygui()
dpg.destroy_context()