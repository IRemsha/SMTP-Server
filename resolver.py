from subprocess import Popen, PIPE


def find_RR_MX(hots):
    with Popen(['nslookup', "-type=MX", hots], stdout=PIPE) as cmd:
        answer = cmd.stdout.read().decode('cp1256')
        _MX_record = answer.split('\n')[3]
        idx = _MX_record.find('mail exchanger = ')
        mail_exchanger = _MX_record[idx + len('mail exchanger = '):-1]
    return mail_exchanger
