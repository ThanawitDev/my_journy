count = 0
with open("garage.txt", "r", encoding='utf-8') as input_data:
    with open("job_order.txt", "w", encoding='utf-8') as output_data:
        
        output_data.write(f"=================Servic Check================\n")

        for line in input_data:
            clean_line = line.strip()
            data = clean_line.split(",")

            models = data[0]
            miles = int(data[1])
            count+=1
            if miles >= 24000:
                service_status = "DESMO SERVICE (Urgent!)"
            elif miles >= 1000:
                service_status = "Oil Change"
            else:
                service_status = "Check up only"
            output_data.write(f"JOB-[{count}]: {models} | Mileage {miles} ---> Status: {service_status}\n")

        output_data.write(f"=================================================\n")
        output_data.write(f"Total {count} processed by System\n")