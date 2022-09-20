import os
import shutil

package_name = "awk"
target_dir = "output-123"

if __name__ == '__main__':
    
    root_path = os.getcwd()

#   HANG
    
    hang_output_dirname = "hang_collect_{}".format(package_name)
    hang_output_dir = os.path.join(root_path, hang_output_dirname)
    if not os.path.exists(hang_output_dir):
        os.makedirs(hang_output_dir)


    for sub_afl in os.listdir(os.path.join(root_path, target_dir)):
        sub_path = os.path.join(root_path, target_dir, sub_afl)
        
        os.mkdir(os.path.join(hang_output_dir, sub_afl))

        for item in os.listdir(sub_path):
            if item == 'hangs':
                hang_path = os.path.join(sub_path, 'hangs')
                for filename in os.listdir(hang_path):
                    file_path = os.path.join(hang_path, filename)
                    output_path = os.path.join(hang_output_dir, sub_afl, filename)
                    shutil.copy(file_path, output_path)

        print("Finish copy hang result for dir {}".format(sub_afl))

#   Crash

    crash_output_dir = "crashes_collect_{}".format(package_name)
    os.mkdir(os.path.join(root_path, crash_output_dir))


    for sub_afl in os.listdir(os.path.join(root_path, target_dir)):
        sub_path = os.path.join(root_path, target_dir, sub_afl)
        
        os.mkdir(os.path.join(root_path, crash_output_dir, sub_afl))

        for item in os.listdir(sub_path):
            if item == 'crashes':
                crash_path = os.path.join(sub_path, 'crashes')
                for filename in os.listdir(crash_path):
                    file_path = os.path.join(crash_path, filename)
                    output_path = os.path.join(root_path, crash_output_dir, sub_afl, filename)
                    shutil.copy(file_path, output_path)

        print("Finish copy crash result for dir {}".format(sub_afl))

#   QUEUE   
    queue_output_dir = "queue_collect_{}".format(package_name)
    os.mkdir(os.path.join(root_path, queue_output_dir))


    for sub_afl in os.listdir(os.path.join(root_path, target_dir)):
        sub_path = os.path.join(root_path, target_dir, sub_afl)
        
        os.mkdir(os.path.join(root_path, queue_output_dir, sub_afl))

        for item in os.listdir(sub_path):
            if item == 'queue':
                queue_path = os.path.join(sub_path, 'queue')
                for filename in os.listdir(queue_path):
                    file_path = os.path.join(queue_path, filename)
                    output_path = os.path.join(root_path, queue_output_dir, sub_afl, filename)
                    try:
                        shutil.copy(file_path, output_path)
                    except Exception as e:
                        print(e)
        print("Finish copy queue result for dir {}".format(sub_afl))
