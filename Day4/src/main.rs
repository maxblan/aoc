use std::fs; 
use std::collections::HashMap;
 
fn main() { 
 
    let contents: String = fs::read_to_string("input.txt")
        .expect("Something went wrong reading the file");

    let split = contents.split("\n\n");

    let mut all_passports: Vec<HashMap<&str, String>> = Vec::new();

    let mut valid_pass_old: i32 = 0;
    let mut valid_pass_new: i32 = 0;

    for i in split {
        let mut single_pass = HashMap::new();
        let sub1 = i.split(" ");
        for j in sub1{
            let sub2 = j.split("\n");
            for k in sub2 {
                match k {
                    k if k.contains("byr:") => single_pass.insert("byr", k.replace("byr:","")),
                    k if k.contains("iyr:") => single_pass.insert("iyr", k.replace("iyr:","")),
                    k if k.contains("eyr:") => single_pass.insert("eyr", k.replace("eyr:","")),
                    k if k.contains("hgt:") => single_pass.insert("hgt", k.replace("hgt:","")),
                    k if k.contains("hcl:") => single_pass.insert("hcl", k.replace("hcl:","")),
                    k if k.contains("ecl:") => single_pass.insert("ecl", k.replace("ecl:","")),
                    k if k.contains("pid:") => single_pass.insert("pid", k.replace("pid:","")),
                    k if k.contains("cid:") => single_pass.insert("cid", k.replace("cid:","")),
                    _ => single_pass.insert("", String::from("")),
                };                
            }
        }

        if single_pass.contains_key("byr")&&single_pass.contains_key("iyr")&&single_pass.contains_key("eyr")&&single_pass.contains_key("hgt")
            &&single_pass.contains_key("hcl")&&single_pass.contains_key("ecl")&&single_pass.contains_key("pid") {
                valid_pass_old+=1;
                all_passports.push(single_pass);
            }
            single_pass = HashMap::new();
    }
    
    for p in all_passports {

        // Get all key values from the hash map.
        let byr = p.get_key_value("byr").unwrap().1.parse::<i32>().unwrap_or(0);
        let iyr = p.get_key_value("iyr").unwrap().1.parse::<i32>().unwrap_or(0);
        let eyr = p.get_key_value("eyr").unwrap().1.parse::<i32>().unwrap_or(0);
        let hgt = p.get_key_value("hgt").unwrap().1;
        let hcl = p.get_key_value("hcl").unwrap().1;
        let ecl = p.get_key_value("ecl").unwrap().1;
        let pid = p.get_key_value("pid").unwrap().1;

        let hair_chars = hcl.chars().nth(0).unwrap();

        let mut all_ifs = 0; 

        // Check the birth year.
        if 1920 <= byr && byr <= 2002 {
            all_ifs += 1;
        }
        // Check the issue year.
        if 2010 <= iyr && iyr <= 2020 {
            all_ifs += 1;
        }
        // Check the expiration year.
        if 2020 <= eyr && eyr <= 2030 {
            all_ifs += 1;
        }
        // Check the height.
        if hgt.contains("cm") {
            let value = hgt.replace("cm","").parse::<i32>().unwrap_or(0);
            if 150 <= value && value <= 193 {
                all_ifs += 1;
            }
        }else if hgt.contains("in") {
            let value = hgt.replace("in","").parse::<i32>().unwrap_or(0);
            if 59 <= value && value <= 76 {
                all_ifs += 1;
            }
        }
        // Check the hair collor. 
        if hair_chars == '#' && hcl.replace("#","").chars().all(char::is_alphanumeric) && hcl.replace("#","").chars().count() == 6 {
            all_ifs += 1;
        }
        // Check eye color.
        if ecl == "amb" || ecl == "blu" || ecl == "brn" || ecl == "gry" || ecl == "grn" || ecl == "hzl" || ecl == "oth" {
            all_ifs += 1;
        }
        // Cheack passport ID.
        if pid.chars().count() == 9 {
            all_ifs += 1;
        }

        // Checks if all ifs where true.
        if all_ifs == 7 {
            valid_pass_new += 1
        }
    }
    
    //.parse::<i32>().unwrap_or(0)
    println!("Valid passports old: {}", valid_pass_old);
    println!("Valid passports new: {}", valid_pass_new);
}