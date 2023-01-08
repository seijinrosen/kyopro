use std::{fs, path::Path};

fn main() {
    println!("input contest name.");
    println!("example: abc284");
    println!();

    let contest_name = rspy::input("type here: ");
    let contest_dir_path = Path::new(".")
        .join("atcoder.jp")
        .join("contests")
        .join(&contest_name)
        .join("tasks");
    let templates_py_path = Path::new(".").join("templates").join("main.py");

    for ch in 'a'..='e' {
        let problem_dir_name = contest_name.to_string() + "_" + &ch.to_string();
        let problem_dir_path = contest_dir_path.join(problem_dir_name);
        problem_dir_path.mkdir_all();
        fs::copy(
            &templates_py_path,
            problem_dir_path.join(templates_py_path.file_name().unwrap()),
        )
        .unwrap();
    }
}

trait MyPath {
    fn mkdir_all(&self);
}

impl MyPath for Path {
    fn mkdir_all(&self) {
        fs::create_dir_all(self).unwrap()
    }
}
